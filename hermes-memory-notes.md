# Hermes Memory System — Research & Reasonix Port Plan

Two artifacts from our conversation:

1. **How Hermes implements its memory system** (research answer, from `hermes-agent-fork`)
2. **Port plan: memory loop only** (approved scope for the `DeepSeek-Reasonix-Fork`)

---

## Part 1 — How Hermes implements the memory system

(from the research into `E:\work\digital-brain\hermes-agent-fork`)

### The storage model — three independent stores

| Store | What it holds | Where |
|---|---|---|
| **Memory files** | Curated durable facts (agent notes + user profile) | `~/.hermes/memories/MEMORY.md` (2,200-char cap) + `USER.md` (1,375-char cap), per profile |
| **Skills** | Reusable procedures | `~/.hermes/skills/<category>/<name>/SKILL.md` + `references/ templates/ scripts/` |
| **SessionDB** | Full verbatim transcripts, FTS5-indexed | `~/.hermes/state.db` (SQLite) |

They deliberately **don't sync** — `MEMORY_GUIDANCE` routes: durable facts → memory, procedures → skills, task progress/artifacts → `session_search` (`prompt_builder.py:173-186`). There's **no TTL** on cards; staleness is handled by char caps forcing consolidation and by guidance ("if a fact will be stale in a week, it does not belong in memory").

### The write path (the self-improvement loop)

Two independent counters, **neither injects text into the conversation**:

- **Memory nudge** — every N user turns (default 10, `memory.nudge_interval`), `turn_context.py:582` sets a `should_review_memory` flag on the `TurnContext`; using the `memory` tool resets the counter.
- **Skill nudge** — every N tool iterations (default 10), `turn_finalizer.py:673` decides `_should_review_skills`.

When flagged, the **finalizer spawns a daemon-thread background review** (`turn_finalizer.py:691` → `background_review.py:635`), but only **after the final response is delivered** so it never competes with your turn. The review is a **forked fresh `AIAgent`** that:

- inherits the parent's provider/model (prompt-cache warmth) but a **toolset whitelisted to memory+skills only**,
- runs with `_persist_disabled=True` (never touches your session DB) and auto-denies dangerous commands,
- digests the transcript: full snapshot on the main model, or on a cheaper aux model keeps the **last 24 messages verbatim** and collapses older turns into one synthetic digest (`background_review.py:122-163`),
- follows structured prompts: memory review saves persona/preferences; skill review prefers *patching an existing skill → an umbrella → a support file → a new class-level umbrella*, with pinned/external/bundled skills off-limits (`background_review.py:170-295`),
- prints a `💾 Self-improvement review:` summary.

**Formats:** MEMORY.md entries are plain prose chunks joined by `\n§\n` (no frontmatter), deduped via `dict.fromkeys` on load, exact duplicates rejected; over-cap adds return a "consolidate now" error (max 3/turn). SKILL.md is `---`-delimited YAML frontmatter, atomically written, and background-review writes are hard-gated (`_background_review_write_guard`) + stamp `created_by: "agent"` in `.usage.json` — **that stamp is what makes a skill curator-editable and graph-visible**. **`/learn`** (`learn_prompt.py:99`) is the on-demand version: one prompt turns a user-described workflow into a single SKILL.md following strict HARDLINE authoring rules (name ≤64 chars lowercase, description ≤60 chars one sentence, `author: Hermes` literal, fixed body order, no invented commands).

### The read path — frozen snapshot, not per-turn retrieval

Memory is loaded **once per session** (`agent_init.py:1602` → `MemoryStore.load_from_disk`), threat-scanned, and **frozen into a `_system_prompt_snapshot`** that's injected into the volatile tier of the system prompt (`system_prompt.py:500-512`) with a usage-% header. The snapshot is **never mutated mid-session** — memory writes land on disk but only refresh the prompt at session start or after compression (`system_prompt.py:576-585`). Rationale: prefix-cache stability (Hermes is heavily cache-tuned).

**Retrieval is separate from the cards:** `session_search` searches *transcripts* in state.db — Latin via **FTS5 ranked by BM25**, CJK via a cjk-bigram index or trigram search (`hermes_state_search.py:925-1350`) — with anchored ±5-line context windows and lineage dedup. The MEMORY.md cards themselves are *not* ranked-retrieved per card; they're injected as the whole block. The only place cards get chunked is the **learning graph** (`learning_graph.py:254`) — built live from SKILL.md frontmatter (`related_skills`) + `.usage.json` + memory cards, used for the Star Map UI, not for prompt retrieval.

### Curation

`run_curator_review` (`curator.py:1496`): a **deterministic pass** (stale→archive transitions with exemptions) always runs; the **LLM umbrella-building pass is opt-in** (default off), gated by interval (default 7 days) + idle time, forks an agent (`skip_memory=True`, `platform="curator"`) that merges siblings into umbrellas or demotes to `references/`, then archives into `.archive/` (never deletes) and rewrites cron skill references. Plus the lighter per-session skill-update pass every `_skill_nudge_interval`.

### Key design choices worth porting

- **frozen prompt snapshot** (cache stability),
- **counters-without-injection** (no prompt pollution),
- **forked review agent with a whitelisted toolset** (safety),
- **write guards + provenance stamp** (curation safety).

---

## Part 2 — Port plan: Hermes-style memory loop (memory only)

Scope chosen by the user: **Memory loop only** — nudge + background review that writes consolidated memory cards into Reasonix's existing memory store (no skills/curator/learning-graph in this port).

### What the port reuses (already in the fork)

- **Memory store** — `internal/memory/store.go`: one-fact-per-file Markdown, types `user/feedback/project/reference`, project/global scope, `Store.SaveWithOptions(m, opts)` with revisioning + MEMORY.md index. Any fact saved there **automatically appears in every future session's system-prompt prefix** (`memory.Compose` at `internal/boot/boot.go:429`) — no extra injection wiring needed.
- **Headless runner** — `routines.AgentRunner` (`internal/routines/runner.go`): `boot.Build` + capturing sink + `ToolApprovalAuto`. A "review this transcript" pass can run exactly like Hermes' forked review agent.
- **Turn-end hook** — `finishGuardedTurn` in `internal/control/controller.go:782` already emits `event.TurnDone` and is the natural place for a nudge counter.
- **Transcript renderer** — `Agent.summarize`/`renderTranscript` in `internal/agent/compact.go:671-770` is a ready template for the review prompt input.

### Assumptions (reversible defaults)

Review writes **project-scoped** facts (all four types; no global/feedback-scope writes in v1 — the `remember` tool's interactive approval gate stays for user-driven writes); the review runs in a detached goroutine on a **fresh session** (no lease conflict with the active session); nudge defaults to every 10 tool-using turns (Hermes' default), configurable.

### Phases

1. **Nudge trigger + config**
   - Add `[memory]` config section: `review_enabled` (default on), `nudge_interval` (default 10), `review_model` (empty = default_model), `min_turns` (default 4), `max_transcript_chars` (default ~40k)
   - Controller nudge counter: increment in `finishGuardedTurn` when the finished turn used tools (`toolWasCalledLastTurn()`); at `>= nudge_interval` fire the review — guarded by in-flight dedup and "not mid-turn"; reset on fire (mirror Hermes' `turn_context.py:582`)
   - Verify: unit test the counter/gating logic with a fake controller

2. **Background review runner (`internal/memoryreview/`)**
   - `Reviewer.Run(ctx, transcript)` → renders the session transcript (from `agent.LoadSession` on the active session path, or `renderTranscript`-style), runs `routines.AgentRunner` with a Hermes-style review prompt: distill durable facts (user preferences, feedback on how to work, project constraints, references) and **output a JSON array** of `{type, scope, name, title, description, body}`
   - Parse + validate the JSON (with a strict fallback: discard malformed entries), dedup against `Store.List()` + `recallIdentityKeys` (update existing facts via revision bump instead of near-duplicates)
   - Persist via `SaveWithOptions` directly (host code — the reviewer intentionally bypasses the `remember` tool's approval gate, matching Hermes' `_persist_disabled` fork)
   - Tests: prompt build, JSON parse/validation, dedup + create/update behavior against a temp store with a fake runner

3. **CLI trigger, wiring, docs, commit**
   - Add `reasonix memory review [--session PATH]` to trigger a review on demand (smoke-test path that doesn't wait for nudges)
   - Wire the auto-nudge into the controller (serve + CLI sessions); ensure the review goroutine is detached and never blocks the turn
   - `docs/SESSION_MEMORY_RETRIEVAL.md` + AGENTS.md note; `go test ./internal/memoryreview/... ./internal/control/...` green, `make build`; commit on `main-v2` and push
   - End-to-end verify: unit suite + a live smoke with the real model on the serve session if the key allows

---

*Saved from the conversation: Hermes memory research answer + approved "memory loop only" port plan for the reasonix-fork.*

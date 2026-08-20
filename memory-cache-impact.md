# Memory Loop — Cache Hit-Rate Impact (utmost priority)

Analysis of how the planned Hermes-style background memory review affects LLM
prefix-cache hit rates in the `DeepSeek-Reasonix-Fork`, plus the amended plan
with cache-safety as hard constraints.

---

## How the prefix cache works here (and why hits are high today)

- The system prompt — instructions + AGENTS/REASONIX hierarchy + **auto-memory index** + skills index — is composed **once per session** and frozen (`internal/boot/boot.go:424-437`). Every turn reuses it as the token prefix → partial prefix-cache hits across the whole session (and, for the shared system block, even across sessions).
- Everything mid-session (memory writes, BM25 recall, background-job notes) deliberately **rides the user-turn tail** — `<memory-update>` is prepended to the input, `<memory-recall>` appended to its end (`internal/control/input.go:183-212`) — extending the request *at the end*, so the shared prefix never changes. The comments say it verbatim: "Mid-session changes never touch this prefix — they ride the controller's transient turn-injection and fold in on the next session."

## Impact of the planned memory loop

| Scenario | Cache-hit impact |
|---|---|
| **Reviewer writes facts mid-session** (current session) | **Zero.** The prefix is frozen; writes only touch the store. Same as the `remember` tool today. |
| **Current session should "see" the new facts** | Still zero — queue notes → `<memory-update>` tail injection (`controller.go:4599` pattern). Tail, not prefix. |
| **Next session after a review wrote facts** | **Bounded, one-time, partial re-warm.** New facts change the auto-memory *index block* inside the system prompt → only the tokens **after the changed line** (memory index + skills index, a small segment) miss once; the instructions/AGENTS block and history still hit. Exactly the cost a manual `remember` pays today — one line per fact (name + one-line description). |
| **The reviewer's own LLM call** | Extra request per nudge (~every 10 tool-heavy turns) — **cost, not hit-rate**. If the review prompt uses the *same* system prefix as the session (Hermes deliberately does this: the fork inherits the parent's runtime for prompt-cache warmth, `background_review.py:46-110`), the review call itself hits the shared system prefix; only the transcript body is novel. |

**Net:** the loop does not hurt cache hits **if** we preserve two invariants the
codebase already enforces: (1) never rebuild the session's system prompt
mid-session, (2) any same-session visibility goes through the tail-injection
queue. The only permanent cost is the same one the user's own `remember`
writes already cause — a small, occasional re-warm of the memory-index segment.

## Amended plan (cache-safety hard constraints baked in)

1. **Nudge trigger + config**
   - Add `[memory]` config: `review_enabled`, `nudge_interval` (10), `review_model`, `min_turns` (4), `max_transcript_chars` (~40k), `review_budget_tokens` guard
   - Nudge counter in `finishGuardedTurn` (tool-heavy turns only), in-flight dedup, fires post-turn only
   - **Constraint A:** the review path never calls any system-prompt rebuild / prefix invalidation — it runs detached, writes only to the store
   - Verify: unit tests for counter + gating

2. **Background review runner (`internal/memoryreview/`)**
   - `Reviewer.Run` → transcript from the session `.jsonl`, review prompt via `routines.AgentRunner` (same workspace/`boot.Build` so the **system prefix is byte-identical → cache warmth** on the review call), JSON output `{type, scope, name, title, description, body}`
   - Parse/validate, dedup vs `Store.List()` + `recallIdentityKeys` (revision-bump updates, no near-duplicates)
   - Persist via `SaveWithOptions` only; **Constraint B:** if the current session should see facts, push `memory.Queue` notes (tail), never touch the prefix
   - **Constraint C:** keep index entries to the store's compact format (name + one-line `Description`) so any re-warm segment stays minimal
   - Tests: prompt build, JSON parse, dedup/create/update, and a cache-invariant test asserting no prefix rebuild is triggered

3. **CLI trigger, wiring, docs, commit**
   - `reasonix memory review [--session PATH]` on-demand trigger; wire the auto-nudge into the controller; detached goroutine, never blocks the turn
   - Docs (`SESSION_MEMORY_RETRIEVAL.md` + AGENTS.md) documenting the cache invariants; `go test ./internal/memoryreview/... ./internal/control/...` + `make build` green; commit + push on `main-v2`

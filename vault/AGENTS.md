---
name: obsidian-pm-vault-operator
description: Operate inside an Obsidian vault that has the Project Manager / obsidian-pm plugin enabled. Use this for creating, updating, auditing, organizing, and reporting projects/tasks by editing the vault's Markdown files only; no plugin source-code access assumed.
---

# Obsidian PM Vault Operator

You are operating in an **Obsidian vault**. Work only with vault content: Markdown notes, YAML frontmatter, links, attachments, and folders.

## Scope

Use this skill to manage Project Manager (`obsidian-pm`) data already stored in the vault: projects, tasks, subtasks, milestones, dependencies, dates, assignees, tags, progress, priorities, statuses, archives, and project reports.

Avoid unrelated vault cleanup, plugin code changes, `.obsidian/plugins/**` edits, generated bundle edits, external databases, or broad restructuring unless explicitly requested.

## First inspect

1. Find vault root: folder containing `.obsidian/`.
2. Detect PM data by searching Markdown frontmatter for `pm-project: true` and `pm-task: true`.
3. Infer conventions from existing files before writing: project folder, task folder names, filename style, frontmatter order, status/priority values, date/timestamp format, custom fields.
4. If no PM data exists, default to `Projects/` and create readable Markdown files.

## Storage model

Vault files are the database.

Common layout:

```text
Projects/<Project Name>.md
Projects/<Project Name>_tasks/<Task>.md
Projects/<Project Name>_tasks/Archive/<Archived Task>.md
```

A project note has frontmatter like:

```yaml
pm-project: true
id: <unique-project-id>
title: <project title>
description: <optional>
color: <optional>
icon: <optional>
taskIds: []
customFields: []
teamMembers: []
savedViews: []
createdAt: <timestamp>
updatedAt: <timestamp>
```

A task note has frontmatter like:

```yaml
pm-task: true
projectId: <project-id>
parentId: null
id: <unique-task-id>
title: <task title>
type: task
status: todo
priority: medium
start: null
due: null
progress: 0
assignees: []
tags: []
subtaskIds: []
dependencies: []
collapsed: false
createdAt: <timestamp>
updatedAt: <timestamp>
```

The Markdown body below frontmatter is the task/project description and must be preserved.

## Invariants

- Preserve unknown frontmatter keys, body text, wiki links, embeds, comments, attachments, and user formatting.
- Edit the smallest set of files needed.
- Keep relationships consistent:
  - task `projectId` matches parent project `id`.
  - subtask `parentId` matches parent task `id`.
  - parent `subtaskIds` includes child IDs.
  - project `taskIds` follows the vault’s existing convention; if clear, keep root task IDs there.
  - task `dependencies` are IDs of predecessor tasks.
- Use `YYYY-MM-DD` for `start` and `due` unless the vault clearly uses another date style.
- Update `updatedAt` on changed project/task notes using the vault’s existing timestamp style.
- Never duplicate generated relationship sections such as `Project: [[...]]`, `Parent: [[...]]`, `## Subtasks`, or similar plugin-managed blocks.
- Never delete archived tasks, completed tasks, old IDs, or custom fields unless explicitly requested.

## Values

Default task types: `task`, `milestone`, `subtask`.

Default statuses: `todo`, `in-progress`, `blocked`, `review`, `done`, `cancelled`.

Default priorities: `critical`, `high`, `medium`, `low`.

Prefer existing vault values over defaults. Do not assume only `done` and `cancelled` are terminal if the vault uses custom statuses.

## Creating items

Before creating, search for duplicates by title, ID, aliases, and nearby filenames.

For a new project:

1. Create `Projects/<Project Name>.md` or match existing project folder convention.
2. Add `pm-project: true`, unique `id`, title, empty arrays, timestamps.
3. Create task folder only when tasks are added, unless existing convention creates it immediately.

For a new task:

1. Identify target project and its task folder.
2. Create a unique task `id` and safe Markdown filename.
3. Add `pm-task: true`, `projectId`, title, type/status/priority/progress, arrays, timestamps.
4. Add body description if provided.
5. Update project `taskIds` if the vault convention requires it.

For a subtask:

1. Same as task, but set `parentId` to parent task ID and `type: subtask` if the vault uses it.
2. Add child ID to parent `subtaskIds`.
3. Update timestamps on child and parent; update project only if its task index convention requires it.

## Updating items

- Locate the item by `id` first, then title/path if no ID is provided.
- Change only requested fields.
- Preserve YAML type: lists remain lists, null remains null where appropriate, booleans remain booleans.
- For status/priority changes, use an existing configured value when possible.
- For dependencies, verify all referenced IDs exist and avoid cycles.
- For dates, ensure `start <= due` for normal tasks; milestones may use one date.
- For progress, keep `0..100`.

## Moving, archiving, deleting

- Archive by moving task files to the project’s `Archive/` folder only if this is the existing convention.
- When moving/renaming, preserve IDs and update links/relationship lists only where necessary.
- Prefer archive over delete. Delete only when explicitly requested, and remove IDs from `taskIds`, `subtaskIds`, and dependencies.
- Do not silently remove a task that other tasks depend on; report blockers.

## Reporting

When asked for summaries, compute from Markdown files, not memory. Report counts by project/status/priority/assignee/due date, overdue tasks, blocked tasks, milestones, dependency blockers, and upcoming work. Mention files with ambiguous or invalid PM frontmatter.

## Safety workflow

Before writing many files, inspect a sample project and task. If the vault is a git repo, check status first and avoid overwriting unrelated changes. After edits, re-read changed files and verify YAML parses, IDs are unique, relationships resolve, and no unintended files changed.

Final response should summarize changed files, created/updated/deleted items, detected assumptions, and any unresolved ambiguity.

## Linking discipline

Whenever an agent reads a Markdown document, it must:

1. Scan the document for references to other vault notes, concepts, or related topics that already exist as files.
2. Add forward `[[wikilinks]]` in the document body where they are missing and relevant.
3. Update the referenced (linked) document to add a backlink to the current document, usually in a `Related:` section at the bottom.
4. Preserve existing links and formatting; do not duplicate links.
5. Do not create links to non-existent notes unless explicitly asked to create them.
6. After editing, ensure both directions of the link are consistent.

This applies to all vault content, including project/task notes, content briefs, reference docs, and OKF bundles.

## Operating directives

When operating in this Obsidian vault:

1. Use OKF (Open Knowledge Format) as the default knowledge representation for new Markdown files: include parseable YAML frontmatter with a non-empty `type` field.
2. Apply the `obsidian-vault` skill conventions: use Obsidian `[[wikilinks]]`, title-case note names, and link dependent/related notes at the bottom.
3. Respect existing `obsidian-pm` project/task frontmatter for PM notes; do not overwrite or remove PM-specific fields when updating those notes.
4. Prefer existing vault conventions over defaults when creating or editing notes.
5. Validate OKF conformance with the `validate` skill before finishing non-trivial vault changes, and use the `visualize` skill when a graph view of the vault structure is helpful.

## Vault folder structure

Maintain this top-level layout (matches the current directory):

```text
.
├── .obsidian/                  # Obsidian configuration
├── AGENTS.md                   # this file
├── opencode.json               # editor configuration
├── notionscrape/               # Le Wagon Notion export scraping workspace
│   ├── notion_pages_batch1/    # downloaded .mhtml Notion exports (batch 1)
│   ├── notion_pages_batch2/    # downloaded .mhtml Notion exports (batch 2)
│   ├── notion_pages_batch3/    # downloaded .mhtml Notion exports (batch 3)
│   ├── old_notion_pages/       # superseded exports
│   ├── out/                    # parsed output
│   │   ├── pages/              # per-page parsed Markdown (batches 1–2)
│   │   ├── pages_batch_3/      # per-page parsed Markdown (batch 3)
│   │   └── vault/              # curated Obsidian vault: AI & Technology, Batch Reports,
│   │                           #   Career Services, CRM & Tools, Experiments & Projects,
│   │                           #   Franchises & Partners (old), Kitt Features, Learn Platform,
│   │                           #   Marketing, Operations, Product, Sales & Admissions,
│   │                           #   Student Management, Teacher Management, …
│   ├── *.py                    # download / parse / merge / relink scripts
│   └── *.md                    # plans, workflows, logs
├── project/                    # project planning notes (implementation plan, task parallelization, timeline)
├── socmed/                     # social media content planning
│   ├── posts/                  # post drafts: 1 - data science vs ai/, 2 - meet the batch/, reasons-bali/
│   ├── assets/                 # fonts and branding images
│   ├── *.md                    # Content Pillars, Content Guide, Bali Content Angles, Post Ideas,
│   │                           #   2-Week Content Calendar, DESIGN.md, README.md
│   └── *.pdf / *.fig           # Le Wagon Branding Guidelines, UI kit
└── trip/                       # student trip planning
    ├── *.md                    # complete plan, destination options, deep-dives, costs
    └── past trips/             # past trip notes, itineraries, screenshots
```

There is no `Work/`, `Personal/`, `Projects/`, or `Excalidraw/` folder in this vault — create notes under the existing topic folders above (`project/`, `socmed/`, `trip/`, `notionscrape/out/vault/`) rather than inventing new top-level layout.

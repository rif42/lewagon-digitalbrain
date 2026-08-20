---
name: lewagon-socmed-vault-operator
description: Operate inside the Le Wagon Bali social media content folder. Manage content briefs, calendars, post plans, and link them to the root obsidian-pm project/tasks.
---

# Le Wagon Socmed Vault Operator

## Scope

This folder contains content strategy, post ideas, content pillars, and post briefs for the Le Wagon Bali social media program.

When working here:

- Preserve existing content notes and their frontmatter.
- Treat the matching Obsidian PM project (`Projects/Le Wagon Bali Content.md` or its tasks) as the source of execution truth.
- Keep content briefs and strategy docs in `Work/Clients/lewagon/socmed/`.
- Keep PM tasks and project files in `Projects/`.
- Link content notes to PM tasks and vice versa; do not duplicate the project management data itself.

## Linking discipline

Whenever an agent reads any document in this folder, or any document that references this folder:

1. Scan for references to related notes already stored as files in the vault.
2. Add forward `[[wikilinks]]` in the current document body where they are missing and relevant.
3. Update the referenced (linked) document to add a backlink to the current document, usually in a `Related:` section at the bottom.
4. Preserve existing links and formatting; do not duplicate links.
5. Do not create links to non-existent notes unless explicitly asked to create them.
6. After editing, ensure both directions of the link are consistent.

## Reference

See the root [[AGENTS.md]] for the full `obsidian-pm-vault-operator` instructions and the global linking discipline.

---
type: notion-import
notion-id: 32f8924af01481a59e33e6c8f70d9694
source-url: https://app.notion.com/p/lewagon/CRM-Architecture-RevOps-Strategy-Le-Wagon-32f8924af01481a59e33e6c8f70d9694
imported: 2026-07-23
---
# CRM Architecture & RevOps Strategy — Le Wagon
 =?utf-8?Q?agon=20|=20Notion?=
This space documents the CRM architecture for Le Wagon's HubSpot setup. It covers the 3-object model, lifecycle stage definitions, reversal decision matrix, standard properties, and automation rules.
> **Status:** Paper model — validated for review, not yet implemented in HubSpot.
> **Last updated:** March 2026 — updated with confirmed object model and real property list.
---
---
## The 3-object model (confirmed)
ObjectTypeRoleContactsNative HubSpotObject #1. Central truth for all segmentation. Every deal and lead links back to a contact.LeadsNative HubSpot Sales HubSales qualification pipeline. Created automatically when a contact scores high enough after a pre-sales call. Inbound only.DealsNative HubSpotTwo pipelines: Application (form steps) and Admission (post-submission process).
---
## Table of contents
SectionWhat's inside01 · Architecture overviewThe 3-object model, how objects relate, inbound entry points02 · Object lifecycle stagesStage definitions for Contact, Lead, Application pipeline, Admission pipeline03 · Reversal & transition rulesThe decision matrix: what happens to the Contact for every exit scenario04 · Standard HubSpot propertiesThe actual property list per object — contacts, leads, deals05 · Automation rulesIF → THEN logic, what's manual, circular dependency checklist06 · Friday workshop prepOpen decisions, meeting agenda, validation checklist
---
## North star
A **regular HubSpot user** should be able to build any contact list or segment using only:
- lifecycle_stage
- 7-10 standard contact properties (campus, program interest, lead type, bootcamp prediction, course interest list etc.)
---
## The 5 core principles
1. **Paper before HubSpot.** The model is defined in writing before any workflow is built/updated.
1. **Contact is object #1.** All segmentation is done on Contacts. Deals and Leads feed the contact's lifecycle — they don't replace it.
1. **Reversals must be explicit.** Every exit scenario (NO GO, abandoned form, no response) has a defined outcome for the Contact. No ambiguity.
1. **No circular dependencies.** Automation flows in one direction. Clear ownership for every property update.
1. **Inbound only.** Le Wagon works exclusively with inbound leads from defined entry points. The model reflects this — no cold outreach flows.
---
[01 · Architecture overview](https://app.notion.com/p/lewagon/01-Architecture-overview-32f8924af0148155bad0dfe472e62243?pvs=25)
[02 · Object lifecycle stages](https://app.notion.com/p/lewagon/02-Object-lifecycle-stages-32f8924af01481fa9900c20451c57ead?pvs=25)
[03 · Transition & reversal rules](https://app.notion.com/p/lewagon/03-Transition-reversal-rules-32f8924af014816c92eccefd950a02b8?pvs=25)
[04 · Standard HubSpot properties](https://app.notion.com/p/lewagon/04-Standard-HubSpot-properties-32f8924af01481638c58f094b566aa5e?pvs=25)
[05 · Automation rules](https://app.notion.com/p/lewagon/05-Automation-rules-32f8924af01481369572d2543c6fc627?pvs=25)
[06 · Friday workshop prep](https://app.notion.com/p/lewagon/06-Friday-workshop-prep-32f8924af01481e2bd59e2f9c143f412?pvs=25)
**Schema (in progress)**
> [!object] https://whimsical.com/le-wagon-marketing/crm-architecture-le-wagon-hubspot-8suJCgyBprGNPmRMGc9Sk8
## Related
- [[Content]]

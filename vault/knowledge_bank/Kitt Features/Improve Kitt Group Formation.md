---
type: notion-import
notion-id: 2fb8924af014807eae0cdb115f539f7d
source-url: https://app.notion.com/p/lewagon/Improve-Kitt-Group-Formation-2fb8924af014807eae0cdb115f539f7d
imported: 2026-07-23
---
# Improve Kitt Group Formation
## 
## Summary
> [!note] 
> TODO: Explain the problem in one sentence. ***Don’t think/talk about a solution ❌***​
## Business Impact
> [!note] 
> TODO : Explain business impact of your issue
**Time & Operational Costs**
- **Teachers spend too much time** supporting unbalanced groups with multiple low-level or struggling students
        -
- **High frequency**: Occurs every bootcamp cycle during the 2-week project phase
        -
- Workaround time cost: Data Analytics Paris team manually collects preferences and manually forms groups (bypassing Kitt entirely) to avoid these issues. It takes them circa 2/3 hours every time in order to do the correct calculations taking into account students’ preferences.
**Student Experience & Satisfaction**
        -
- **Relational friction** arises when students with known interpersonal difficulties are grouped together, creating tensions that affect the overall class atmosphere.
        -
- **NPS impact:** Students regularly mention group-related issues in their end-of-bootcamp feedback, directly affecting satisfaction scores.
        -
- Unbalanced technical distribution impacts the overall class experience as teacher attention becomes unevenly distributed
        -
- Risk to completion rates when struggling students are clustered together without adequate support structure
        -
- Paris campus has been **manually circumventing the algorithm for 12+ months, **other campuses do the same. This is a strong indicator that this is not an isolated case.
        -
## Context & Problem
> [!note] 
> TODO: Explain in great details the context surrounding this issue
Current Process: Pitch Night & Group Formation
1. Students attend pitch night where project ideas are presented
        1.
1. Each student ranks all pitches in order of preference via Kitt
        1.
1. Kitt's algorithm calculates group assignments based on individual preferences
        1.
1. Groups are immediately published and visible to students (no review step)
        1.
The algorithm operates in isolation: it optimizes for preference matching but is blind to the factors teachers rely on to build effective teams:
- **Technical balance: **struggling students can end up clustered in the same group
        -
- **Interpersonal dynamics: **students with known relational difficulties may be grouped together
        -
- **Pedagogical judgment: **there is no room for the "human factor" that makes groups work
        -
- **Time spent** on reforming groups according to all factors above
        -
### **→ Add an Intermediate Review Page to Kitt?**
**New workflow**:
1. Students rank their preferences (unchanged)
        1.
1. Kitt algorithm calculates optimal groups based on preferences
        1.
1. **→ NEW STEP**: Results displayed on a Kitt “**review page”** for the project manager. Not visible to student, group shouldn’t be revealed yet.
        1.
1. Project manager can:
        - Approve groups as-is if they're well-balanced
                    -
        - Make adjustments to optimize team balance (still respecting preferences as much as possible)
                    -
1. Once approved, groups are published and visible to students
        1.
## Related

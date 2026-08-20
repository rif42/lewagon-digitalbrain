---
type: notion-import
notion-id: 3728924af01480ebb014f4435cf1d080
source-url: https://app.notion.com/p/lewagon/Kitt-Attendance-Centralizing-Presence-Lateness-Tracking-Across-Cities-3728924af01480ebb014f4435cf1d080
imported: 2026-07-23
---
# Kitt Attendance: Centralizing Presence & Lateness Tracking Across Cities
## Summary
*A*ttendance tracking is currently managed through fragmented, external tools that are unreliable, inconsistent across cities, and time-consuming for Ops teams to maintain.
## Business Impact
- **Time lost by teams:** Ops staff spend significant recurring time chasing teachers to fill in their Google Sheets or Forms. This is a repetitive, manual overhead that could be fully eliminated.
        -
- **Data reliability:** When teachers forget to log attendance, information about late arrivals and absences becomes incomplete or impossible to retrieve after the fact, making student follow-up very difficult.
        -
- **Accumulated absences & lateness:** Tracking patterns over time (repeated lateness, accumulating absences) is critical for student support, but currently nearly impossible to do reliably with scattered tools.
        -
- **Legal & audit compliance:** Germany in particular has strict audit requirements (exact duration of lateness must be recorded). Non-compliance is a legal risk.
        -
- **Missed sync opportunity:** An absence form already exists but is not connected to attendance data, creating duplicate effort and information silos.
        -
## Context & Problem
Attendance tracking is supported in Kitt by students checking themselves in / Edusign -they have to sign even if they were absent to acces Kitt / for LW to be paid in France. As a result, cities and formats have independently built their own workarounds, typically Google Sheets or Google Forms to match Ops needs and legal attendance requirements, all structured differently and none integrated with Kitt. This creates several cascading issues:
1. **Teachers forget to fill in the sheet or form.** Ops teams must regularly remind them, consuming time that should be spent on higher-value tasks.
        1.
1. **Edusign is not a full substitute.** Edusign requires the student's signature to venter Kitt, meaning an absent student simply can sign, and the data shown in Kitt is inaccurate. Additionally, Edusign does not capture late arrivals.
        1.
1. **No visibility on lateness.** Ops needs to track which students arrived late (rule of 5 late maximum during the bootcamp), but this is invisible in Edusign. Germany needs to track both absences and the exact duration of lateness for legal audit purposes. Online batches need simple, reliable attendance tracking without the complexity of Edusign.
        1.
1. **Fragmented information.** When a student is absent or late, Ops and teachers have to dig through multiple tools to piece together the history, which is time-consuming and error-prone. If absences or lateness accumulate, it's very hard to catch it in time to support the student.
        1.
1. **No connection to the absence form.** There is currently an absence declaration form, but it is completely disconnected from attendance logs, requiring double handling.
        1.
**Examples of current tools used by cities:**
- 🇫🇷 **France (Paris):** [Google Form batch 2272 ](https://docs.google.com/forms/d/e/1FAIpQLScpLLHWUFQMZjRDByf3wqrGveV1RiOJ_XOUWviiLERpOAO1Fw/viewform)- Notion explicatif: [[Vérification Ponctualité Batchs Paris|🙋Vérification Ponctualité Batchs Paris]]
        -
- 💻 **Online: **batch [FT 2300](https://docs.google.com/spreadsheets/d/19Z-f8w4EnfiuHYnSkz7YAc2B4x2uRE4H/edit?gid=1239863617#gid=1239863617)
        -
- 🇩🇪 **Germany:** [FT 2026](https://docs.google.com/spreadsheets/d/1bqBtYtgxGbgcr2Vp5f8NGPTqQBSqhloAgiUqtK_te1A/edit?pli=1&gid=2002888747#gid=2002888747)
        -
**Ideal end state -I know we are not supposed to-:**
A teacher should have to record attendance once per day on Kitt, in the morning, directly in Kitt, marking each student as present, absent, or late, and logging the duration of lateness. This data should be centralised, easily accessible to Ops, and so for audit and ideally synchronised with the existing absence form, serving both legal audit requirements (Germany) and general student follow-up across all formats and cities.
Also the scope here would be FT - PT potentially-, seems complicated to already implement in Flex
---
## Related
- [[Attendance tracking]]

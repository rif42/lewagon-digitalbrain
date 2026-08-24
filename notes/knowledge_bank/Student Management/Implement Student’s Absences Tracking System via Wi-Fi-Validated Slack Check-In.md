---
type: notion-import
notion-id: 2f18924af014800dbb25e8429679b52a
source-url: https://app.notion.com/p/lewagon/Implement-Student-s-Absences-Tracking-System-via-Wi-Fi-Validated-Slack-Check-In-2f18924af014800dbb25e8429679b52a
imported: 2026-07-23
---
# Implement Student’s Absences Tracking System via Wi-Fi-Validated Slack Check-In
## Summary
> [!note] 
> TODO: Explain the **problem** in one sentence.
Current attendance tracking (Signing on Kitt ) fails to identify late arrivals and absences in real-time for large Paris batches, preventing timely intervention and enforcement of attendance policies.
## Business Impact
> [!note] 
> TODO : Explain **business impact** of your issue
<details><summary>**Suggested Checklist**</summary>
</details>
**Revenue Risk:**
- Students who disengage early (undetected absences/lateness) are more likely to drop out, impacting completion rates and potential refund requests. Furthermore, students who are not engaged in the bootcamp have a negative impact on other students’ experiences, during the bootcamp and mostly during the projects.
        -
- Poor attendance enforcement damages Le Wagon's reputation in general.
        -
- This also has an impact on Teachers’ satisfaction and performances. Teachers found it harder to manage students that are not engaged and involved in the bootcamp.
        -
**Operational Costs:**
- Staff spends excessive time on manual attendance tracking instead of high-value student support
        -
- Teachers are overburdened at 9am, reducing focus on pedagogy quality
        -
**Student Outcomes:**
- Late intervention on struggling students reduces their chances of success
        -
- Disengaged students disrupt batch dynamics, affecting overall cohort performance and satisfaction (NPS impact)
        -
**Compliance & Legal:**
- Inability to enforce contractual attendance terms weakens our position in case of disputes
        -
**Scalability:**
- Current manual process doesn't scale with growing batch sizes (Paris batches now 35-50 students)
        -
- Limits our ability to improve Paris operations without proportionally increasing staff headcount
        -
**Estimated Impact:**
- Between 5-10 hours/week of staff (Program Manager&Campus director) time wasted on manual tracking per large batch. Which eventually does not prove to be as efficient as a tracking tool since it is the teachers who communicate which students are there and which are not.
        -
- Potential 10-15% increase in student success rates with early intervention
        -
## Context & Problem
> [!note] 
> TODO: Explain in great details the context surrounding this issue
<details><summary>**Suggested Checklist**</summary>
</details>
### **Current Manual Process:**
**Scale of the problem:**
In Paris, we manage batches of 35-50 students (130 students total this quarter), making manual attendance tracking operationally impossible. Since students sign on Kitt even though they are not physically present on campus, disrupting the bootcamp experience.
**Daily workflow breakdown:**
1. **9:00 AM - Teachers attempt visual tracking**
        - Teachers try to identify absences while setting up lectures and answering early questions
                    -
        - With 35+ students, it's nearly impossible to accurately track who's absent AND who arrives late
                    -
1. **Throughout the day - Incomplete reporting**
        - Teachers report absences they noticed to staff via Slack
                    -
        - Late arrivals (students slipping in after 9am) are rarely caught or reported
                    -
        - Data is incomplete and inconsistent
                    -
1. **Staff manual consolidation**
        - I spend significant time (5-10 hours/week) following up with teachers
                    -
        - Manually tracking patterns across multiple batches
                    -
        - Cross-referencing with student signatures on Kitt and attendance tracking
                    -
1. **Delayed intervention (Week 4-5)**
        - By the time we identify problematic patterns (multiple absences and late arrivals), habits are already established
                    -
        - Multiple students are routinely late/absent
                    -
        - Without early action, students assume there are no consequences
                    -
**The cascade effect:**
- Students see peers arriving late without consequences → lateness becomes normalized
        -
- More students start arriving late or missing days
        -
- Batch dynamics deteriorate, disrupting the formation for everyone
        -
- Staff lacks data to enforce contractual attendance requirements
        -
- Teachers become frustrated managing attendance instead of focusing on pedagogy
        -
## **📸 Specific Examples**
### **Example 1: AI Software Bootcamp Paris (Recent Quarter)**
- **Context:** Batch of 28 students
        -
- **Issue identified:** Multiple students with chronic lateness only detected in Week 5
        -
![](https://app.notion.com/image/attachment%3A027f35ba-3c3d-4df2-8a96-b41b5085bb78%3ACapture_decran_2025-12-10_a_11.48.31_AM.png?table=block&id=2f18924a-f014-80f8-8217-e862abc6925e&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/attachment%3Af46c182e-bb08-4550-831a-800ac3847992%3ACapture_decran_2025-12-10_a_11.48.55_AM.png?table=block&id=2f18924a-f014-80a7-b23a-d601b67c0ecc&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
- **Root cause:** Teachers were attentive, staff was monitoring, but we couldn't systematically track all absences/late arrivals at scale
        -
- **Outcome:** Late intervention, behavioral patterns already established, difficult corrective conversations. In a particular case, a motivated student, Moïse, found himself by himself most of the times because his group classmates were always late and not involved in the bootcamp.
        -
![](https://app.notion.com/image/attachment%3Ad332878c-11da-4ffc-950a-aba1facdaf10%3ACapture_decran_2025-12-10_a_11.49.53_AM.png?table=block&id=2f18924a-f014-80e7-a8a0-eb7005170205&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### **Example 2: Data Science Q4 2025**
- **Context:** 50 students in total
        -
- **Challenge:** Really difficult to manually track at this scale
        -
- **Impact:** Delayed identification of at-risk students, missed opportunity for early support
        -
### **Why existing solutions don't work:**
**Edusign (current legal tool):**
- ✅ Works for funding/compliance (students sign to prove enrollment)
        -
- ❌ Can be signed remotely (doesn't prove physical presence)
        -
- ❌ No operational visibility for staff
        -
**Operational Pains : **
When we have to keep track of 130 students at the same time, we find ourselves investing a lot of time in keeping track of students's absences and late arrivals. The teachers always try to do their best and they tell me daily who is absent but, with batches with more than 35 students, it is difficult to tell who is absent and also very difficult to know who is late each morning.
This has a big impact on the good unfolding of the bootcamp since, if we don't know about a student's absence or late arrival, I cannot act on it. If I don't act on it, by week 4/5, we have multiple students arriving very late, and since we took no actions or we did but only seldomly (since we did not know about all of them), the students see no consequences in arriving late or missing a few days and it happens more often than it should, consequently disrupting the good unfolding of the formation. This is why it would be so useful to implement a tool like this, at least for Paris, with whom we can track students absences in a more straightforward way without having to rely on teachers. So that we can act on them and I can make sure that the students are respecting the contract and are invested in the bootcamp.
We feel like it would be a much needed tool that could improve students (since we would act on those who misbehave in a faster and more efficient way), teachers (that would not have to worry about it) and staff's(it would be easier to track everything and therefore act on it) experience.
Lastly, it would allow us to have, for those rare cases in which we would want to expel the students, (internal) proof that they were not there, even though they signed on Kitt. I can further elaborate on it, if you wish, let me know.
**Propositions :**
We would like to explore a new attendance check-in workflow that is simple, reliable, and hard to bypass. The idea is to leverage Slack + campus Wi-Fi verification, with automatic data sync to Airtable (or similar).
Proposed Workflow :
1. Slack Check-In Button
        - Each morning, students check in using a Slack button inside their batch channel.
                    -
        - The check-in is only validated if the student is connected to the campus Wi-Fi (via IP or SSID verification).
                    -
1. Automatic Data Capture
        - Once validated, the system automatically logs data into Airtable (or similar):
                    -
        - Student name
                    -
        - Batch
                    -
        - Timestamp
                    -
        - Status (present/late/not validated)
                    -
1. Automations
        - Automatic alerts for late or missing check-ins
                    -
        - Daily dashboard for staff
                    -
        - Early detection of “weak signals” (patterns of lateness/absences)
                    -
1. Optional Add-On
        - After check-in, display a quick emotional check: “How are you feeling today?”
                    -
    → Helps teachers/TAs identify students who may need extra support.
⸻
Benefits
- Reliable and frictionless daily check-in
        -
- Hard to cheat (must be physically on campus / using campus Wi-Fi)
        -
- Zero hardware required
        -
- Easy and familiar for students (Slack-based)
        -
- Valuable insights for pedagogy team
        -
⸻
Next Steps
- Validate feasibility of Wi-Fi/IP verification via Slack app
        -
- Define Airtable (or similar) schema
        -
- Estimate development effort
        -
## Other Resources
> [!note] 
> TODO: Link to your internal teamspace pages if any
## Related
- [[Attendance tracking]]
- [[Automations]]

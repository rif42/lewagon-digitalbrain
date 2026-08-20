---
type: notion-import
notion-id: 2018924af014808a9443ea8343a05729
source-url: https://app.notion.com/p/lewagon/Automated-Slack-Reminders-for-Gathertown-Sessions-2018924af014808a9443ea8343a05729
imported: 2026-07-23
---
# Automated Slack Reminders for Gathertown Sessions
## Release note 🚀​
[[Notify online lectures & livecode on Slack|🔔Notify online lectures & livecode on Slack]]
## Summary
> [!note] 
> TODO: Explain the problem in one sentence. ***Don’t think/talk about a solution ❌***​
Currently, reminders for upcoming sessions (including Gathertown campus links) using Slack workflow automation. This results in 2 to 10 automated messages per batch. The process is repetitive, time-consuming, and prone to error. Automating these messages directly from Kitt, as was done previously with Zoom, would improve consistency and efficiency across SC, PT, and FT online batches.
## Business Impact
> [!note] 
> TODO : Explain business impact of your issue
<details><summary>**Suggested Checklist**</summary>
</details>
- Significant time lost by Program Managers setting up multiple Slack automations per batch.
        -
- Risk of errors or missed reminders causing confusion for students and missed or late attendance.
        -
## Context & Problem
> [!note] 
> TODO: Explain in great details the context surrounding this issue
<details><summary>**Suggested Checklist**</summary>
</details>
For every batch (SC, PT, FT), Program Managers currently post reminders before each session, including:
- The Gathertown campus link
        -
- The session’s teacher(s)
        -
- The attendance Google Sheet
        -
This is done using Slack workflows.
Previously, Zoom links and session data were automatically posted via Slack from Kitt. A similar system should be implemented for Gathertown to ensure consistency, reduce operational load, and improve student readiness and experience.
Additionally, the current reminders do not include the name of the teacher leading the session, which used to be part of the automated Zoom reminders. While this is manageable, especially for online batches where students often see different teachers and assistants, reintroducing this detail where relevant (e.g. for full-time sessions) would enhance clarity.
The current process messages we use : [No access](https://app.notion.com/p/47828e78c1a34bb19e027f492f6ac73b?pvs=24#47828e78c1a34bb19e027f492f6ac73b)
What the messages looks like :
FT BC
![](https://app.notion.com/image/attachment%3Abcf05047-384c-4460-8413-bf1cef9b1c3b%3AScreenshot_2025-05-28_at_18.35.39.png?table=block&id=2018924a-f014-80d4-910e-e42eae1c5a80&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/attachment%3Ad8d46050-a1d2-4d5f-b23f-d5870c71b297%3AScreenshot_2025-05-28_at_18.36.06.png?table=block&id=2018924a-f014-80dd-93ea-f8d81fe385c6&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
SC Bootcamp
![](https://app.notion.com/image/attachment%3A51f6023b-c6c9-4fa7-a9d6-1b8a49b470b7%3AScreenshot_2025-05-28_at_18.36.55.png?table=block&id=2018924a-f014-8068-b9df-f4dffb0f5a9e&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/attachment%3Af07e19ab-84cc-43d1-a938-c56ed552a842%3AScreenshot_2025-05-28_at_18.37.23.png?table=block&id=2018924a-f014-8036-b18e-c6b592ce8838&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
PT Flex Bootcamp
![](https://app.notion.com/image/attachment%3A1ecd7bb0-b47b-4206-b99b-1a2b739c3cda%3AScreenshot_2025-05-28_at_18.36.28.png?table=block&id=2018924a-f014-80b7-8229-de2eabb7e8d1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related
- [[Automations]]
- [[Notify online lectures & livecode on Slack]]

---
type: notion-import
notion-id: f1768815202244d58851f1e536a6900e
source-url: https://app.notion.com/p/lewagon/SA-Ops-Handover-Extract-Key-Info-in-CSV-f1768815202244d58851f1e536a6900e
imported: 2026-07-23
---
# SA <> Ops Handover - Extract Key Info in CSV
## Context
When handing over students to Operations and Batch managers, Online best practices include giving some essential information about each student to ensure the best experience for both sides.
The info usually included warnings about the students (not responsive), location (if problematic timezone), specific personal situations (kids at home) ***collected during the interview & after*****. **Specifically for Online, teachers won’t be able to get to know the students the same way as in person.
It was also found to be helpful to include some additional information about each applicant in the handover to Ops, including:
- Nationality
- Country of residence
- Interview fit (stars)
- Admissions quiz score
- Prep work completion
This way of handover has proved extremely valuable, but collecting all this information manually was painful and time-consuming.
## Solution
Within the ATS Grid view, we have a pre-existing Export applicants as csv action 👇​
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb9c79457-0d8a-4b68-9fbf-aa2a70040498%2FScreenshot_2023-06-27_at_18.10.04.png?table=block&id=4acfb400-1f07-4887-98b1-822f587df536&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Which we have enhanced to include the additional key information about each applicant 👇​
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F56c78998-ba0d-441c-b415-c0247f0fe3b8%2FScreenshot_2023-06-30_at_10.33.46.png?table=block&id=d823937d-810a-4c48-92c4-532480c668a6&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!note] 
> *If you are adding these exported students to a Learn batch,**** please keep info only to First, Last Names and Email.
****The extra columns uploaded on Learn could expose students sensitive data to external teachers.*
> [!note] 
> The blank Comments column is to be filled in by the Admissions managers, with any key points of information about the applicant learned during the interview or after, which would be insightful for the Ops teams to know
## Related
- [[Best practices]]

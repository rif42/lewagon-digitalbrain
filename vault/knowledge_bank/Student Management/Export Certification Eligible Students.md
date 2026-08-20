---
type: notion-import
notion-id: 3748924af01481c9829ddce3bcb2728d
source-url: https://app.notion.com/p/lewagon/Export-Certification-Eligible-Students-3748924af01481c9829ddce3bcb2728d
imported: 2026-07-23
---
# Export Certification Eligible Students
## Context
The ops team currently relies on an outdated Google Sheet to manage convocation lists for French certification (RNCP) exam sessions. This sheet cannot be filtered by city, batch number, or contract type, making it increasingly difficult to identify eligible students accurately — especially as the eligibility rule shifts to target all students with a French contract. Additionally, some students in online French-speaking batches (based in Switzerland or Belgium) are not eligible for French certification and must be easily excluded from convocation lists.
---
## Solution
### Filtering Capabilities
The Assess-ready export will be paired with a Metabase [dashboard](https://metabase.lewagon.com/dashboard/490-eligible-students?batch_start=&batch_end=&course=&campus=&batch_slug=&invoicing_campus=) supporting filters by batch number, city, French contract status, program, and start/end date — replacing the outdated Google Sheet entirely.
![](https://app.notion.com/image/attachment%3A68093dca-f30a-4613-8a07-d84452868e30%3AScreenshot_2026-06-03_at_14.00.27.png?table=block&id=3748924a-f014-8063-9714-f3f79bf0fd75&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Direct CSV Export
Ops team members will be able to export an Assess-compatible CSV directly from the dashboard, eliminating manual data preparation steps ahead of each certification session.
### Process
1. Select the students eligible based on your filters then click on **B2C FR & Online students since 2025 export**
    ![](https://app.notion.com/image/attachment%3Ad43004f1-1bec-403b-93f2-6dcb542935d4%3AScreenshot_2026-06-03_at_14.03.15.png?table=block&id=3748924a-f014-801e-a16e-fbd6480dbaaa&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1330&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
1. Click on the ☁️ ⬇️ download icon then choose **.csv**
    ![](https://app.notion.com/image/attachment%3Ab4a0dc09-c194-49f5-979e-8f5cb2e374a1%3AScreenshot_2026-06-03_at_14.03.59.png?table=block&id=3748924a-f014-8002-b2ff-efc0fbb15285&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1330&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> ⚠️ **Deadline reminder:** The next certification session is scheduled for **June 17–18, 2026**. Please ensure the Metabase dashboard is validated and ready before that date.
---
**Stakeholders:** Ops team (certification/RNCP onboarding)
## Related
- [[Assess]]
- [[Onboarding]]

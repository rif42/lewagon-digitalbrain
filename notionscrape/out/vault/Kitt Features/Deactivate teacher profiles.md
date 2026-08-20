---
type: notion-import
notion-id: 1fc8924af014804fac3cf27682eafdcc
source-url: https://app.notion.com/p/lewagon/Deactivate-teacher-profiles-1fc8924af014804fac3cf27682eafdcc
imported: 2026-07-23
---
# Deactivate teacher profiles
## Context
The Ops team deals with staffing & teachers on a daily basis and similar to the student flags ([[At-risk Student Tracking|🚩At-risk Student Tracking]]), may need to keep tabs on certain teachers and keep a history of this within Kitt.
There are many contexts : sometimes they may want to keep the teacher but add a comment about them, or they may want to disable the teacher’s profile entirely with an explanation for why the teacher was disabled. This history should be accessible to employees so that the Ops teams have all information available to them.
## Solution
There is a new section available to **city managers **in a teacher’s profile where their status and history will be accessible:
![](https://app.notion.com/image/attachment%3Ac28c3ab9-3b24-4648-abd0-362b8468870b%3AScreenshot_2025-05-23_at_13.56.35.png?table=block&id=1fc8924a-f014-807a-a25d-d5f2d5e29db1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
This section will allow city managers to either add generic comments about a teacher:
![](https://app.notion.com/image/attachment%3A01c5aa28-6b80-4973-803f-fd6cb5a93777%3AScreenshot_2025-05-23_at_15.11.40.png?table=block&id=1fc8924a-f014-80f1-ac37-e2bbaea11867&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/attachment%3A7434431b-a273-4c0b-8606-601fd97dc038%3AScreenshot_2025-05-23_at_15.12.35.png?table=block&id=1fc8924a-f014-8042-b9e9-e46fee0d0f7f&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Or request to deactivate this teacher’s profile:
![](https://app.notion.com/image/attachment%3A016a27b6-79e7-45db-9ac6-acc36e4fab39%3AScreenshot_2025-05-23_at_15.13.17.png?table=block&id=1fc8924a-f014-809d-a7a1-d6e5e855644a&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Deactivation request
Once a deactivation request has been made, a message will be sent to a Slack channel in order to alert the Ops team about the request:
![](https://app.notion.com/image/attachment%3Ab2f0f251-a259-4cf1-961f-3e7f5c3469f4%3AScreenshot_2025-05-23_at_13.17.59.png?table=block&id=1fc8924a-f014-8063-8820-ca13b316dfdf&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
From there, the Ops team can review the request and choose to **deactivate the account** or to **keep the account. **
ℹ️ If deactivate is chosen, the account will immediately be disabled and the teacher will no longer have access to Kitt batches **where they were a teacher** (they’ll still have access to their batch if they are an alumni).
![](https://app.notion.com/image/attachment%3A27d11d8a-9d4b-4e85-8e89-5ab963911919%3AScreenshot_2025-05-23_at_15.16.54.png?table=block&id=1fc8924a-f014-80d0-8175-de24ebb98229&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Upcoming work days
If the teacher still has **upcoming work days, **the Ops team will be unable to confirm the deactivation until the teacher has been removed from the relevant calendars:
![](https://app.notion.com/image/attachment%3A44f4d59f-4c66-4cbe-b899-0207ce93be09%3AScreenshot_2025-05-28_at_16.03.26.png?table=block&id=2018924a-f014-80aa-a39f-fcdbdef375dd&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Keeping the teacher
If the Ops team decides to keep the teacher, they will be prompted to add a comment explaining why they’re retaining the teacher:
![](https://app.notion.com/image/attachment%3A0acc4d83-ed08-48bb-88b7-ca47856c5931%3AScreenshot_2025-05-23_at_15.17.21.png?table=block&id=1fc8924a-f014-802d-82ed-e6761d7dfb9a&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Once a choice has been made, the original requester will receive a Slack message with the response:
![](https://app.notion.com/image/attachment%3Ab95dab85-f0e7-4e4f-b9b8-cf04890a3275%3AScreenshot_2025-05-23_at_13.18.04.png?table=block&id=1fc8924a-f014-8053-b815-e5e18bf7daed&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Deactivation
If the deactivation is confirmed, the teacher will lose access to all programs they had been granted, and will be removed from the relevant teachers- slack channels and github orgs.
### Reactivation
If a teacher has been deactivated, the history will remain visible to city managers and a Reactivate CTA will be available:
![](https://app.notion.com/image/attachment%3A29b5b2c5-c7b5-4793-8d76-36b08232454b%3AScreenshot_2025-05-23_at_13.57.58.png?table=block&id=1fc8924a-f014-801a-8294-e4d370052d99&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
This will immediately restore the teacher’s profile and they will again have access to Kitt’s teacher features (batches/calendars, invoicing, etc).
### Screen recording of entire flow:
> [!video] 
### External vs alumni:
- If the teacher is an **alumni**, they will lose access to the teachers- channels in Slack but retain access to the general alumni Slack. They will retain access to Kitt but only their student side, they will lose any views related being a teacher.
- If the teacher is **external,** they will lose access entirely to alumni Slack and Kitt.
## Related
- [[At-risk Student Tracking]]
- [[Slack Channels]]

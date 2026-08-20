---
type: notion-import
notion-id: 2238924af01480f490edc455d8bbbff7
source-url: https://app.notion.com/p/lewagon/Notify-online-lectures-livecode-on-Slack-2238924af01480f490edc455d8bbbff7
imported: 2026-07-23
---
# Notify online lectures & livecode on Slack
## Context
Until now, Slack notifications sent 15 minutes before online lectures or livecodes were tightly coupled with Zoom events. Meanwhile, the Ops team had set up custom Slack workflows for each batch channel in GatherTown. Now that Zoom is no longer used and everyone has migrated to GatherTown and Google Meet, we need a unified, automated way to notify users before their sessions.
This PR introduces a system that automatically sends Slack notifications to users ahead of their online lectures, livecodes, and helpdesks, restoring a feature that was lost during the Zoom-to-GatherTown transition.
## Solution
Automatic Slack notification have been re-implemented, following the same pattern than before the migration from Zoom to GatherTown or Google meet.
### **Full-time batch **
Notifications will be sent in the students' Slack channel:
- 15min before the day is supposed to start
    ![](https://app.notion.com/image/attachment%3A3bf00e29-5f62-4cd2-808a-8fd9cc4bdf4b%3ACapture_decran_2025-07-09_a_09.08.01.png?table=block&id=2238924a-f014-80b7-b1b4-fcaed9d3c920&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1330&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
- also 15min before Livecode/recap start.
    ![](https://app.notion.com/image/attachment%3A3a761914-6cbb-40b7-8f1f-89d3a25b3467%3ACapture_decran_2025-07-09_a_10.41.04.png?table=block&id=2268924a-f014-80f3-a773-cb7fac378a3d&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1330&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### **Part-time & Skill courses batch **
A notification will be sent 15 minutes before each session in the students' Slack channel:
![](https://app.notion.com/image/attachment%3A361e2939-4127-4371-b72e-3e0d93e4a5f8%3ACapture_decran_2025-07-09_a_10.50.52.png?table=block&id=2268924a-f014-80b7-a525-f94ff15466e3&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
⚠️ Livecode/recap notifications have been removed, as these sessions don't always occur. Teachers should manually notify students in the Slack channel when a livecode/recap is planned.
### Flex Batch
For Flex Part-Time, the previously automated **daily summary** notification has been kept:
**Flex Daily Summary**** **
![](https://app.notion.com/image/attachment%3A2e1fe141-f5c4-4213-8fb9-dd4ab3d0a0fe%3ACapture_decran_2025-07-09_a_11.12.49.png?table=block&id=2268924a-f014-80e9-a704-e6d19fe29ccf&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Two new notifications have been introduced—sent 15 minutes before sessions—to encourage students to join campus:
- **Flex Livecode**
![](https://app.notion.com/image/attachment%3A6f548f6b-af6d-4ac5-bbbe-efae233b20ec%3ACapture_decran_2025-07-09_a_10.58.13.png?table=block&id=2268924a-f014-80b8-a734-eac392e27c7e&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
- **Flex Helpdesk**
![](https://app.notion.com/image/attachment%3A933750b0-906f-4904-8ea8-454583fc7773%3ACapture_decran_2025-07-09_a_10.59.41.png?table=block&id=2268924a-f014-806e-ad7c-e52a27f6c313&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related
- [[Events]]
- [[Skill courses]]

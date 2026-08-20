---
type: notion-import
notion-id: 2b98924af01480169543c85ca3764c82
source-url: https://app.notion.com/p/lewagon/Tracking-students-for-referral-program-2b98924af01480169543c85ca3764c82
imported: 2026-07-21
---
# Tracking students for referral program
### Blazer queries
There are two Blazer queries to track which students (and which referrers) should soon receive a gift card:
- [Applies with a referral link where the batch ends in the next 3 weeks](https://kitt.lewagon.com/blazer/queries/2440-applies-with-referral-link-except-wagoner-where-camp-ends-in-3-weeks)
- [Applies with a referral link where the batch ends in exactly 3 weeks](https://kitt.lewagon.com/blazer/queries/2441-applies-with-referral-link-except-wagoner-where-camp-ends-in-exactly-3-weeks)
The second query runs every day and if there is a match, it will throw a notification in the #referral-program Slack channel which looks like this:
![](https://app.notion.com/image/attachment%3A206fd4bc-5e34-4815-9a01-3ae038de8359%3AScreenshot_2025-11-28_at_09.12.48.png?table=block&id=2b98924a-f014-80fe-b25a-ebf8e5dc97ab&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!note] 
> As this query runs every day, there will be no results anymore the day after. This is why the other query is useful to keep an overview of all the students whose batch will end within the next 3 weeks.
### Identifying the referrer
On the Blazer queries, there is a link to the referral link on [Avo](https://www.lewagon.com/admin/resources/referral_links). From there, the referrer can be identified.
![](data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7)
### **Slack notifications**
Notification on #referral-program should be enabled so that they are not missed. They should be set to All new posts.
![](https://app.notion.com/image/attachment%3A9cd7c14f-83f4-4c95-9200-15a7b3076b85%3Ascreenshot_2025-11-27_at_11.11.11_720.png?table=block&id=2b98924a-f014-809c-88d2-f3c225036773&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### **Onboarding new members**
If other people than admins, @Baptiste Derenne or @María Jesús Torres should have access to the Slack channel or the Blazer queries, they can be added to the channel. To get access to the queries, a ticket on help should be opened as new people need to be added to the Flipper feature ([here](https://kitt.lewagon.com/flipper/features/blazer:query:2440) and [here](https://kitt.lewagon.com/flipper/features/blazer:query:2441)).
## Related
- [[Baptiste Derenne]]
- [[Onboarding]]

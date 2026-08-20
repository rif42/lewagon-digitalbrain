---
type: notion-import
notion-id: 3a0aff9c25324977a21911bd310e5cb5
source-url: https://app.notion.com/p/lewagon/Students-offboarding-3a0aff9c25324977a21911bd310e5cb5
imported: 2026-07-23
---
# Students offboarding
## Context
In our current UI it is not very clear how to offboard a student from a batch and as a result many request for this action land on the help repository. It is also only possible for admins to offboard someone from a skill course.
## Solution
> [!note] 
> The user flow showed below has changed since we released [[At-risk Student Tracking|🚩At-risk Student Tracking]].
You can refer to this FAQ in the Operations Playbook[[Operations FAQ|❓Operations FAQ - How to move a student to Batch 0 / Exclude from buddies or p…]] for the updated process.
We created clearer actions on the **Students** page to differentiate offboarding and moving to parking a batch 👇​
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F3e0d11f0-a284-4d8e-8208-d927cd2a44eb%2FScreenshot_2023-12-05_at_11.12.36.png?table=block&id=67225865-0021-4020-a241-66aa45d420c5&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Parking a student
If the course has a parking batch associated to it (eg, Batch #0 for Web Development, Batch #00 for Data Science etc), a student can be moved to this parking batch if they plan on rejoining the course at a later stage.
The same form has to be filled out as before, and a Slack notification will be sent to the operations channel of the city which the student is moved from.
> [!note] 
> Since [[At-risk Student Tracking|🚩At-risk Student Tracking]] you need to create a flag to park a student
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F85c4c2f3-2578-4759-9b54-7bf9a541dc63%2FScreenshot_2023-12-05_at_11.26.15.png?table=block&id=1b91b95e-e1bb-48f2-afc0-5426fae0b140&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F968d39cc-466e-43b9-95e1-ae1d6bbfc84b%2FScreenshot_2023-12-05_at_11.25.26.png?table=block&id=7d051b34-ba17-4bf6-9a03-b17b66c9a6b5&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Reonboarding a student
On the **Students** page of a parking batch, core users can now see all students who were moved there, rather than just the ones they had moved themselves. This should make it easier to re-onboard students to another batch in the future.
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F81e8b6e5-5195-4ff2-b9fb-c3beff211197%2FScreenshot_2023-12-14_at_14.32.39.png?table=block&id=de40d2a1-85fd-4107-83bc-bf69ce94c97a&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!object] https://teamwagon.slack.com/archives/G3FPKARL4/p1708360828414159
### Offboarding a student
There is a **new page** with a form to fill out to **completely offboard** a student from a batch. 🆕 Students can also be offboarded through this action from a skill course.
If a student is part of another batch on Kitt, they will keep their access to Kitt and Slack as an alumnus/a of this batch. Otherwise their account will be disabled.
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F00b2b4b7-d85f-41a2-99e4-063b671160be%2FScreenshot_2023-12-05_at_11.12.36_(1).png?table=block&id=fdc3a3eb-dc93-4761-aa6a-6e84190ad6d9&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fdce85f01-9c41-4510-b7a8-0663ae70edb7%2FScreenshot_2023-12-14_at_14.38.23.png?table=block&id=81ce2192-bb1d-4b85-9b67-fce78efef133&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related
- [[Archive]]
- [[New page]]
- [[Onboarding]]
- [[Operations Playbook]]

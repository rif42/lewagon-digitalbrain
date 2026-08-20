---
type: notion-import
notion-id: 7d9bd20e151043bda3e2a5e6cc784159
source-url: https://app.notion.com/p/lewagon/At-risk-Student-Tracking-7d9bd20e151043bda3e2a5e6cc784159
imported: 2026-07-23
---
# At-risk Student Tracking
## Context
Le Wagon’s revenue and its reputation is highly dependent upon student satisfaction. This crucially depends on Operations’ ability to track students, which is currently very difficult, because once a batch has started, there is no way to:
1. write notes about students at risk of dropping out or having other issues;
1. access notes made by the admissions teams, which remain in ATS;
1. smoothly offboard students in such a way as to maintain their satisfaction, even following a drop-out.
Existing ad-hoc mechanisms, oral interventions and pure guesswork are not scalable and put Le Wagon at risk. Crucially, Le Wagon’s reputation can be directly harmed if these issues are not addressed.
## Solution
A new batch dashboard is added in the Operations context to flag at-risk students, and is available for admissions team to flag candidates from the start of the admissions process.
> [!note] 
> Note: the student flags feature is currently in **beta, **and will only be enabled for a select number of batches before being rolled out globally.
### **Student Flags**
Flagging students will now start from within the ATS: as S&A managers move through the application process with a student and need to note important details about the potential student, they will now have a new CTA within the candidate’s profile to Add a flag:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F23eb6fd7-44b7-48d8-8366-ab114c8b2f04%2FScreenshot_2024-02-23_at_16.09.20.png?table=block&id=70fbe31e-5d8e-4ed4-9ac9-58253b906ce7&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Clicking Add a flag will take you to the new student flags dashboard for that particular camp, where you can add 1) one or more flag types to the student, 2) assign a city or batch manager to the issue, and 3) add a comment with detailed information:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fc5bcf999-5135-4110-a511-7558905586b1%2FScreenshot_2024-02-28_at_16.38.59.png?table=block&id=22e6b902-ea04-4039-ae7c-b328c871a632&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
From the table view, each flag will appear as a row with key details, as well as a link to open the detailed flag history view:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F772a1dbb-c77e-4183-a172-430e31b85431%2FScreenshot_2024-02-28_at_16.41.07.png?table=block&id=b5d80c79-9f00-4971-9949-f9332b2e3a7a&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fa20a6d6b-9a6a-4f11-8dbe-7e65846dc5a4%2FScreenshot_2024-02-28_at_16.48.41.png?table=block&id=26d4742e-4a76-41fe-8be9-f85b8f054341&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Flags can have additional comments (added by any city or batch manager), as well as being edited to add or remove flags, and change the assigned to:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F1ae6e69f-1e7b-427d-bd95-4eb030157500%2FScreenshot_2024-02-28_at_16.41.45.png?table=block&id=ccacd359-1724-4594-a21f-36cd927adfe6&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F0b4c5db1-bf79-4bf7-b2ff-e27615867966%2FScreenshot_2024-02-28_at_16.55.26.png?table=block&id=5a4b0aa3-2425-4434-8ed8-dd7ba2810a05&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Back on the Apply’s page, the flag is displayed along with a link to view the flag’s details within the batch’s flags dashboard:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F8f9508fd-e971-4f38-a913-bbbf3fe41805%2FScreenshot_2024-02-28_at_17.41.43.png?table=block&id=7e914a2e-e6ed-43a5-9e1f-4c934a2c1420&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Ops Tracking:
Once the handover from S&A <> Ops occurs, the Ops team can then continue to use the dashboard to track students that have previously been flagged, as well as adding new flags.
> [!note] 
> **Note**: a student can have multiple flags associated with them, in case it is important to separate out different concerns related to the student / assign different managers to different issues.
**Flag history:**
In order to keep an accurate history of a flagged student, **all changes / ** **activities** related to a flag will be tracked and displayed within the history view:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F7552231f-cec5-4f35-b80d-1957f126da92%2FScreenshot_2024-02-28_at_18.08.48.png?table=block&id=7050c932-63f6-4f02-adab-47ace6da9b63&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!video] 
**Additional actions:**
Once the batch starts, each flag has some additional actions that can be taken:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F5e4f3183-b3ec-4c4b-89c5-f508f802d669%2FScreenshot_2024-02-28_at_18.10.40.png?table=block&id=6704ce88-a036-4871-b3dc-9f234bff1c19&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!note] 
> For batches with student flags enabled, it is now **required to first add a flag** **before you can park or offboard a student.**
If it is needed to exclude the student from buddies / projects, this can be done from the actions, and additional flags will be added related to these details for the student:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Ff3876428-c33a-4b72-acb8-d2f0acde3dd5%2FScreenshot_2024-02-28_at_18.10.49.png?table=block&id=a64e788b-9364-4381-bf85-50bf67494581&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F510a7d57-4366-434b-a3ae-2e510e0f88a8%2FScreenshot_2024-02-28_at_18.13.20.png?table=block&id=0f9bbcc1-1135-48ac-9872-023712b14d5c&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Offboardings
From the same dashboard, we have provided another view to display all students from this batch that have been dropped or parked, including their final revenue and reason:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fe41aa0ef-df80-4da7-beb1-6b10208d0356%2FScreenshot_2024-02-28_at_17.27.21.png?table=block&id=4c96eda3-e802-47c5-b666-e52322aa06cd&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
The flag history for an offboarded student is still accessible from the additional actions:
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fed4f4b5a-5fe8-49bd-8f96-d8e54e221b56%2FScreenshot_2024-02-28_at_17.29.59.png?table=block&id=4de042f8-e44a-43e1-b689-79a9fe73ebcc&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F9be15ac5-cbe1-43c2-a23e-5148bf9aee4c%2FScreenshot_2024-02-28_at_17.29.41.png?table=block&id=3565a092-fa9e-4e99-9b99-d6cf47a5797e&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related
- [[Candidates]]
- [[Student Flags feature]]
- [[Student flags dashboard]]

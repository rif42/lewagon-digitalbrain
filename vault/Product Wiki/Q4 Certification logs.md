---
type: notion-import
notion-id: 01144d7b95bb40919c45c71e5eb644e1
source-url: https://app.notion.com/p/lewagon/Q4-Certification-logs-01144d7b95bb40919c45c71e5eb644e1
imported: 2026-07-21
---
# Q4 Certification logs
### Students have difficulties to submit large files
@Jérémy Barbedienne warn me that several student encountered difficulties to submit their Figma file during the Web Dev exam session ([406](https://assess.lewagon.com/exam_sessions/406)) 👇​
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fcfe466e6-5802-4761-bf12-846281c5c50f%2FScreenshot_2023-12-21_at_17.18.02.png?table=block&id=3f2c79b2-8ff8-4c4c-b84e-2311c6bf6ad1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
I guess we should:
- Re-enforce the communication around the challenge. Students needs to understand that we only want a prototype in black and white, not a complete mockup.
- Inform students that file greater than 40mn can’t be uploaded
- Add a validation if the file is too large
### Repos not created
2 or 3 students didn’t do a Kitt connect to join the session. In consequence, Assess were not able to create repo in advance.
I had to relaunch this code 👇​
```
User.find_by(github_nickname:"A54P")Candidate.find_by(user:user,exam_session_id:405).create_repos​
```
I guess we should re-enforce communication around that.
### Web dev students without subjects
The five last candidates onboarded didn’t have subjects.
The use_subjects boolean was set to false.
---
After investigation it appears it was due to the change we made to adapt Assess for Skill Course certification exam.
> [!object] https://github.com/lewagon/assess/pull/705
I forgot to run the post-deploy script, reason why the last onboarded students didn’t get any subject 🙇 (because the use_subjects is set to false by default and the session have been created before we deploy)
In order to prevent this in the future I created a new blazer check to warn the engineering team.
[assess.lewagon.comhttps://assess.lewagon.com/blazer/queries/25-web-dev-exam-session-where-use_subjects-is-false](https://assess.lewagon.com/blazer/queries/25-web-dev-exam-session-where-use_subjects-is-false)
### User has change his GH nickname
It happen from time to time, that a student change is GitHub nickname in between his onboarding on Assess and the starts of the exam.
In consequence, Assess isn’t able to invite him to the repo and the following error is raised 👇​
[appsignal.comhttps://appsignal.com/lewagon/sites/615ab5d53b6e07127aba5db3/exceptions/incidents/81/samples/timestamp/2023-12-21T08:00:24Z](https://appsignal.com/lewagon/sites/615ab5d53b6e07127aba5db3/exceptions/incidents/81/samples/timestamp/2023-12-21T08:00:24Z)
To fix the error:
- @Jérémy Barbedienne asked him change back his GitHub nickname
- I add to relaunch this worker 👇​
    ```
    Github::InviteUserToRepoJob.perform_later(25963)​
    ```
I guess we should re-enforce communication before the session to avoid this kind of issue. It’s important to insist that **students shouldn’t change their GitHub nickname** before the start of an exam on Assess.
## Related
- [[Assess]]
- [[Candidates]]
- [[Onboarding]]

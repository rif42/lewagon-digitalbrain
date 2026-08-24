---
type: notion-import
notion-id: 5007b3e3816e4fdcbad012ff182b2861
source-url: https://app.notion.com/p/lewagon/Draft-Form-for-testing-YAML-without-db-forms-files-5007b3e3816e4fdcbad012ff182b2861
imported: 2026-07-23
---
# Draft Form for testing YAML without db/forms files
## Context
The content team has to add and edit several forms and even for a preview they have to go through the engineering team to commit anything to the repo or redeploying Forms.
This practice is lengthy and provides a lot of friction for the workflow.
## Solution
The purpose of this feature is to provide more autonomy to the Content team on adding and editing forms. The feature will enable users to test the UX of a form and provide feedback before contributing to the repo and submitting a PR.
The new feature includes a DraftForm model that stores the YAML content. Creating a new Draft Form is easy, and users can add variables and items to the form.
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Facbf4f20-d5fc-499b-b43b-32d3869c74ca%2FUntitled.png?table=block&id=a351e678-6c5e-47b8-aecd-7ffd192dca4f&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
The feature enables users to create a new Response from the Draft Form's "show" view and fill out the form as a user. Users can then view the responses linked to a Draft Form via a scope in ActiveAdmin. Additionally, deleting a draft form will delete all linked responses to clean up the form.
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fe371aaba-831e-46ea-a9c2-ad26efb07f27%2FUntitled.png?table=block&id=ff7fbbdd-f6bf-4962-a81d-7f6d8b88441d&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!note] 
> Please note that this feature is only for testing the rendering of YAML. A form cannot be used officially until it is committed to db/forms in the GitHub repository and deployed.
## Related
- [[Content]]

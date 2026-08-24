---
type: notion-import
notion-id: 154a2295353444158acf1e5cf12731df
source-url: https://lewagon.notion.site/How-to-Preview-Content-Changes-on-Kitt-154a2295353444158acf1e5cf12731df
imported: 2026-07-23
---
# How to Preview Content Changes on Kitt?
> [!note] 
> This process only concerns Track Owners and will only be accessible by them.
> This feature respond to the current pain: Freelancer content writers have a hard time suggesting changes on our content Github repositories, because there is no easy way to preview the way changes will render on Kitt.
### **Preview content w/ a set of repositories**
This feature adds the ability to preview the content by setting a combination of Github repositories and branches, to catch problems before merging content pull requests.
This comment provides a link to a new **Program Preview** feature within the **Content Admin** section of Kitt:
![](https://lewagon.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F65150357-fe00-4ce4-a602-2a70d31a6345%2FScreenshot_2024-02-01_at_15.40.00.png?table=block&id=80ef82ce-e485-433d-9dc4-1db57081abdb&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=2000&userId=&cache=v2&imgBuildSrc=requestProxiedImageUrl)
💡 Depending on the content to preview and on the program, some fields can be left empty, more info in this Wiki: [Program content repositories](https://www.notion.so/Program-content-repositories-4f0274347d954e8bb088a4fbeb20dcc2?pvs=21)
Once all needed repositories have been selected, the program preview can be generated and the content member can confirm that their changes are working as expected:
> [!video] 
### **Automated link on content pull requests**
As a shortcut to the previewing feature, we have implemented a workflow that will automatically comment on the content Pull Request w/ the appropriate link:
![](https://lewagon.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F3b50fc5a-4672-462b-b9ed-26eb7a81a881%2FScreenshot_2024-02-01_at_16.35.12.png?table=block&id=ce55f69b-3a29-4b38-8d1c-99a3fd79da52&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=2000&userId=&cache=v2&imgBuildSrc=requestProxiedImageUrl)
By clicking the link in the Pull Request comment, the correct repository and branch is already pre-selected in the form
---
### Alerts
Each view within the program preview includes a toggle with the information about the combination of repositories used, as well as a link to go back to the form and edit the repository combinations:
![](https://lewagon.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Ffc875c5c-038e-4a6e-90d2-45c33b37d32b%2FScreenshot_2024-02-01_at_17.17.13.png?table=block&id=9d470cec-f0ff-456f-9478-11622172cbd3&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=2000&userId=&cache=v2&imgBuildSrc=requestProxiedImageUrl)
If no syllabus is chosen or is invalid, the user will be redirected to the form with an alert:
![](https://lewagon.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F9d4d8b02-68f5-46b4-b264-f0ebbce12ae1%2FScreenshot_2024-02-01_at_17.18.24.png?table=block&id=1e33e278-9f9d-4be2-9aba-bb14e5bc132c&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=2000&userId=&cache=v2&imgBuildSrc=requestProxiedImageUrl)
If the combos chosen don’t pair nicely together and the Readmes cannot be displayed, an alert is shown that the readme cannot be found:
![](https://lewagon.notion.site/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fac1d3064-3661-4224-8398-4eb80eb185dd%2FScreenshot_2024-02-01_at_17.47.33.png?table=block&id=1acd793e-c704-4657-bd23-6c871b9b7200&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=2000&userId=&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related
- [[Content]]

---
type: notion-import
notion-id: 2238924af014804f90b3e327fc70eafd
source-url: https://app.notion.com/p/lewagon/Required-teaching-contracts-2238924af014804f90b3e327fc70eafd
imported: 2026-07-23
---
# Required teaching contracts
## Context
Some teachers are staffed without a signed contract, leading to compliance and billing issues. The current **Teaching Contracts dashboard** is not reliable—it's hard to spot missing contracts and it doesn't factor in billing cities. As a result, some teachers work without valid contracts.
Additionally, certain cities fall under the same legal entity and any contract from cities under the same legal entity should be considered valid but this was not reflected in Kitt.
## Solution
In order to improve the visibility over the current state of teachers teaching contracts, the following changes have been implemented.
**Required Tab**
The required tab contains all the teachers which are staffed on the selected year but where the contract procedure has not been started. Contract can only be created for the ongoing year otherwise, the CTA is not available.
![](https://app.notion.com/image/attachment%3A63b9e624-a551-45d5-9956-98d5ecf0d862%3AScreenshot_2025-07-09_at_10.10.53.png?table=block&id=22b8924a-f014-8067-a39b-e0b3a7ebd388&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/attachment%3Abee2dd57-07b2-4f88-a397-084c58010d64%3AScreenshot_2025-07-09_at_09.38.44.png?table=block&id=22b8924a-f014-80b3-9639-f28d390cbeae&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/attachment%3A552ab39c-a4e8-4c76-97c0-36298cf89edb%3AScreenshot_2025-07-09_at_09.39.06.png?table=block&id=22b8924a-f014-800a-ae2a-da589c42f118&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
**In Progress Tab**
An intermediary tab “In Progress” has been added, where all the teachers with a contract “pending” or “signed” are listed. The CTA to copy document upload link has also been added here, to make it easier for CMs to send the send the link and have the teacher complete the process.
CMs can also see the city at the origin of the contract and the latest contract type.
**[France example]**
If a teacher has already started the contract creation process in another city under the same legal entity (Le Wagon SAS), they will now appear in the "In Progress" tab of your city, indicating the city where the contract originated. You will not be able to send them another contract : no more duplicates 👌​
![](https://app.notion.com/image/attachment%3A6d4a3a31-524e-40ca-b20a-729b89990c7d%3AScreenshot_2025-07-09_at_09.39.53.png?table=block&id=22b8924a-f014-803c-abd2-ed13bc5c6f51&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
**Active Tab**
The active tab now only contains the contracts that have been completed.
![](https://app.notion.com/image/attachment%3A1e7138f8-d952-4acb-b891-9d785a816665%3Aimage.png?table=block&id=2238924a-f014-809e-b4c1-f66ce718657c&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
**Year Filter**
On all tabs of the dashboard, users can now filter the view by the year of the teaching contract.
![](https://app.notion.com/image/attachment%3A20f59463-84db-42bc-ac66-7637a91b58cd%3ACleanShot_2025-07-01_at_14.43.26.png?table=block&id=2238924a-f014-8092-aeb7-c7c29bbceba1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
**New Contract Validations**
When a new contract is being created, there is now an automatic validation that occurs when a teacher is selected / the role is changed. If the teacher already has a contract that is valid for the legal entity and the selected role, a warning appears and the form is disabled.
![](https://app.notion.com/image/attachment%3A2dc52ca2-7783-47bf-9f0f-58d255cebc81%3AScreenshot_2025-07-07_at_10.41.23.png?table=block&id=22b8924a-f014-8090-9fea-d91852fe6c50&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!video] 
**More reliable contract information in batch crew page**
The crew page for a batch’s calendar has been updated to include more & better information around the teaching contract. First, we have added a City to bill column in order to make it clearer right away which city the teacher’s will be billing when invoicing. Additionally, based on the city to bill, the Teaching Contract column now display’s accurate information about the teaching contract status.
![](https://app.notion.com/image/attachment%3Ab724838d-e32d-4f68-90aa-9226d2ae9f7f%3AScreenshot_2025-07-30_at_15.21.50.png?table=block&id=2408924a-f014-80e3-a65c-fd21e2e12765&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
If a batch happens to span 2 years — most likely PT / flex batches — then the crew page will also take that into account when displaying the validity of the teaching contract. Depending on the work days of the teacher in the calendar, it will list the teaching contract for each relevant year.
![](https://app.notion.com/image/attachment%3A8299c2e1-4f7a-49d7-ae8b-a47c3f255adb%3AScreenshot_2025-07-30_at_15.19.48.png?table=block&id=2408924a-f014-8067-b638-dde2f7ac874e&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related

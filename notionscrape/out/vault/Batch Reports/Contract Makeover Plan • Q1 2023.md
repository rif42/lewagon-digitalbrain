---
type: notion-import
notion-id: dbbca9ff3bf94d8fb8d82a0da10af2d7
source-url: https://app.notion.com/p/lewagon/Contract-Makeover-Plan-Q1-2023-dbbca9ff3bf94d8fb8d82a0da10af2d7
imported: 2026-07-23
---
# Contract Makeover Plan • Q1 2023
> [!note] 
> **Several changes** in the past have made it so that we need to update our training contracts (e.g. deposit policy; age removal from contact form; new financing options).
The doc below everything you need to do to put your region up to speed with all the changes and to revamp your contracts.
It gives you a simple checklist to be done by **January 27th **✅
## 1. Context on all changes ✏️​
---
**Section 1** gives you **TL;DR on all problems **faced and solutions implemented; **Section 2 **a simple **step-by-step walkthrough** on Notion and Loom on how to edit your contracts
### 1.1 Collecting Age on Contracts 👵​
---
- **Context: **We’ve stopped collection the age of applicants in the apply form - to reduce attrition and apply form length.
- **Problem: **Still, having this information is valuable for: 1) making sure that the applicant is over **18 (or 21)**; 2) splitting batches into two, in case of two classes to have a balanced batch in terms of age.
- **Solution Implemented**
    > DocuSign now collects the age input of all applicants that is then reverted back to KITT in the age field and displayed in the GO page.
    > Additionally, a new mandatory interview field confirms if the student is over 18
    > **Release notes: **[[Collect age in ATS via Docusign|🌱Collect age in ATS via Docusign]]** **
### 1.2 Standardizing Deposit 💰​
---
- **Context: **With the new [No access](https://app.notion.com/p/07d79e55cfaf463abc9036b4987a290f?pvs=24#07d79e55cfaf463abc9036b4987a290f) launched, deposits are set based on the price of a “camp” (= program in a city)
- **Problem: **This difference will require all contracts where cities change deposit to change, as it not currently a variable on KITT, but a value written manually in each contract - in both number and read text.
- **Solution Implemented: **
    > The deposit is now sent when you create / edit a new batch through a new feature. This feature #CAMP_DEPOSIT needs to be added on contracts instead of the deposit value
    > **Release notes: **[[Deposit Amount Variable|💶Deposit Amount Variable]]​
### 1.3 New Financing Options in Europe💲​
---
- **Context: **New financing options are being implemented across multiple campuses
- **Problem: **These new options require for special agreements / legal text to be made in payment clauses.
- **Solution Implemented: **
    > New payment articles are available to be added
    > **Release notes:** [No access](https://app.notion.com/p/403cf808e08140958a8fd10bd3c7c96c?pvs=24#403cf808e08140958a8fd10bd3c7c96c)
### 1.4 Tripartite Contract Agreements
---
- **Context: **Engineering together with legal have launched the tripartite contract agreements as to account for edge cases when the payer of the bootcamp is not the person attending it.
- **Problem: **According to global finance, a few edge cases are needed to be accounted here, however.
- **Solution Implemented: **
    > Tripartite agreements templates are now available to be duplicated on the contract agreement case. These should be used when there is a contract with a student and there’s a company that is paying for the student’s tuition
    > **Release notes: **[[Tripartite Training Agreements|3️⃣Tripartite Training Agreements]]** **
## 2. Step-by-step changing contracts 🙏​
---
The changes and the contract templates you’ll end up having below are the same across all programs (Data Science / Data Analytics / Web Development). We’ll use the example of Web Development, and you just need to replicate this process for the other courses you’re offering.
### 2.1. Updating your standard FT normal payment contract [#core] ⚙️​
---
**Valid for all #core regions & franchises**
- Start with the **normal** payment contract you have. This should be a contract for full-time with** no financing options**, following the cadence of deposit + rest of tuition 1 week before the bootcamp.
- In the first section, where the contract reads “***The trainee identified as follows***”, please add the following:
    <details><summary>Text to add for **collecting age**</summary>
    </details>
- When in the editing mode for the template, go to the “***Tuition Fee and payment schedule article***”
- On this article, you should add the $CAMP_PRICE & $CAMP_DEPOSIT variables
    <details><summary>Text to add for **deposit** & **price**</summary>
    </details>
    <details><summary>PS: Make sure you’ve set the deposit for each batch (👇🏼 Table in the Operations ⚙️)</summary>
    </details>
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F00a31588-6115-4f84-8a9d-ddeceba6c1c3%2FCaptura_de_ecra_2023-01-03_as_17.04.56.png?table=block&id=c9b2e2d6-c654-4382-8de9-0bca2c8a350c&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F791f57d4-4114-4f1d-8aff-3277f6aeac3f%2FCaptura_de_ecra_2023-01-03_as_17.09.58.png?table=block&id=51c2e218-5f48-491e-afe4-80a5fb358d30&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fdc81570b-2839-48d0-8c52-ac6bc097faaa%2FCaptura_de_ecra_2023-01-03_as_17.10.09.png?table=block&id=cb9e45e6-c48d-4937-9aba-83eec793a69f&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!video]
### 2.2 Creating new contracts for new financing options [Europe]💰​
---
After you’ve changed the normal FT template, you’re ready to add the financing options.
**Valid for all European regions with new financing options**
- Click on “New Contract Template” and select the right program. Go to the edit section
- **From the Template Contract selected herein (link below) or from the contract you just updated**, copy and paste the text to the edit version of this new template - this **guarantees that you have all the regiona**l / local **information** you need and the most updated version vs the template from KITT.
- Please see the 2023 template library 👉🏻​
        - [Web Dev](https://drive.google.com/drive/folders/1l968SKN2s1sDy82VkttgMqZgKZo3NqZX?usp=sharing)
        - [Data Science](https://drive.google.com/drive/folders/1CuW1b_Z8Vm-7kmFtBU11plDaxN3fSgp3?usp=sharing)
        - [Data Analytics](https://drive.google.com/drive/folders/1sTcTCsU4v2lYYuCUCNI5zglFXGcpsBD-?usp=sharing)
        - [Skill Courses](https://drive.google.com/drive/folders/1ZuG2HSJlS27uCR5NBUlUMu1lxMZK9oK2?usp=sharing)
- Now, go back to the payment article “***Tuition Fee and payment schedule article***” and delete the text. You should paste the versions below:
    <details><summary>Text for **Alma (Bootcamp)**</summary>
    </details>
    <details><summary>Text for **Alma (Skill Courses) **- Cf. legal Notice</summary>
    </details>
    <details><summary>Text for **Quotanda** Spain, Online and Germany</summary>
    </details>
    <details><summary>Text for **Quotanda** Portugal</summary>
    </details>
- **Release notes:** [No access](https://app.notion.com/p/403cf808e08140958a8fd10bd3c7c96c?pvs=24#403cf808e08140958a8fd10bd3c7c96c)
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7b1dd4c2-de97-4a34-b53b-2804b3bcafd7%2FCaptura_de_ecra_2023-01-03_as_17.20.18.png?table=block&id=96fb2644-0852-4d31-ae39-0f87056e26fe&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F250cff3a-0909-4f95-80b5-c36e0a98cb11%2FCaptura_de_ecra_2023-01-03_as_17.15.34.png?table=block&id=d25a56a1-542f-4ce1-92f2-1687ab13d181&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!video]
*.*
### 2.3 Other contract templates - Tripartite & Data Analytics [#core] 📝​
---
For **Data Analytics training,**** **make sure that you create the same templates as above (No financing + one for each financing option you have).
**Valid for all #core regions**
- You can **check the regular Data Analytics template **by clicking on “New contract template” and selecting Data Analytics.
- Other than the course presentation, you should copy and paste your local information from your other contracts.
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F7b1dd4c2-de97-4a34-b53b-2804b3bcafd7%2FCaptura_de_ecra_2023-01-03_as_17.20.18.png?table=block&id=092d4d9c-335b-4391-8fdc-f6ffe197ff2a&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
For **tripartite** **contracts ****- **mandatory to be sent in case **a company is paying** for an applicant - we recommend that you only do them on a case-by-case basis, as you most likely won’t have them for all courses (WD vs DS vs DA).
- In case you need them, you should create a new template with “Tripartite Template” set as yes
- You can check more info how to move forward from the release notes here: [[Tripartite Training Agreements|3️⃣Tripartite Training Agreements]]
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbab23ae8-08a0-450f-95f3-424d0cff8944%2FCaptura_de_ecra_2023-01-03_as_17.17.44.png?table=block&id=c293eac8-a104-43ce-be4b-b34c2c386110&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## 3. Final Checklist ✅​
---
Use the checklists below at the end of your makeover to make sure everything is covered 🙌​
**Individual contracts**
- [ ] WD FT contract with regular payment schedule
- [ ] WD FT contract **per** financing option
- [ ] DS FT contract with regular payment schedule
- [ ] DS FT contract **per** financing option
- [ ] DA FT contract with regular payment schedule
- [ ] DA FT contract **per** financing option
---
**Per contract****, all below should be updated:**
- [ ] Age variable paragraph added on data collection in the beginning on trainee identification
- [ ] Payment article with $CAMP_DEPOSIT variable used to set deposit and $CAMP_PRICE variable used to set price
**You should have specific contracts ****per program**** in case you offer:**
- [ ] Alma
- [ ] Quotanda
- [ ] Any other financing option
**You should be prepared to create a template for:**
- [ ] Tripartite agreements in case a company is paying for the fee
> [!note] 
> In case you have any questions or doubts regarding this, reach out on #core-admissions-sales 🙌​
## Related
- [[Collect age in ATS via Docusign]]
- [[Deposit Amount Variable]]
- [[Skill courses]]
- [[Tripartite Training Agreements]]

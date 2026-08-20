---
type: notion-import
notion-id: 9a4e9ceb87c247c9ad21ef295fe6b2e6
source-url: https://app.notion.com/p/lewagon/Sunsetting-Minijobbers-9a4e9ceb87c247c9ad21ef295fe6b2e6
imported: 2026-07-23
---
# Sunsetting Minijobbers
This document is a follow-up of the following Help request:
> [!object] https://github.com/lewagon/help/issues/4328
## Context
Minijobber support was first added to Kitt under the request of the old German leadership (Rich and Rhett) to comply with the regulatory changes on our Operation models of relying on Freelance teaching staff.
It was shipped in early 2021, you can read the original Engineering pitch here:
[No access](https://app.notion.com/p/9e07646e089048a98f2371004b7d1bf4?pvs=25)
[![](https://app.notion.com/images/external_integrations/github-pull-merged-icon.png)#4307Feat minijobbers![](https://app.notion.com/images/external_integrations/github-pull-merged-icon.png)Merged](https://github.com/lewagon/kitt/pull/4307)​
Since its infancy, this feature has been very high-maintenance for the Engineering team, with multiple follow-up pitches and monthly Help requests:
[[Minijobbers Payslips]]
[[Minijobber Computation Updates]]
[[Minijobber Profile|🇩🇪Minijobber Profile]]
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F6a5423d5-fc9a-4930-8485-0b1ad993e125%2FUntitled.png?table=block&id=7dd3dd37-1327-47b5-b612-1acb87a8f6de&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F61c79f9f-4487-4a66-96d8-cece74b23e06%2FUntitled.png?table=block&id=97fdf521-04c5-4496-8ca4-219f390bdfd1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Observation
Help request [#4300](https://github.com/lewagon/help/issues/4300) is the occasion to completely rethink the approach with have on the Minijobber IT situation. With the experience we now have, we can say that **building a Minijobber feature in Kitt was a bad idea:**
- It’s a bit far from the core value of Kitt (supporting students from Apply to Outcomes)
- It’s a feature built for only one country
- It’s trying to emulate a pay system with rules that change often based on German Law / Government decisions. There are many SaaS out there trying to just solve Payroll, we are a Coding School, we can only do much worse
- It has burnt out a few devs of Engineering team, suffering from the “hot potato” syndrome
- It’s trying to systematize a process where a lot of Human (and human mistakes or last minute updates) is involved.
## Moving Forward
The latest help request outlines that despite all the hours put by Engineering trying to build this, we fall short, and it’s time to pull the plug, pivoting to a new approach.
👉 **Let’s move Minijobber contract handling out of Kitt**.
We have already done this with a few departments (New Content using an external LMS, Outcomes building their CRM with Hubspot and relying on [huntr.co](http://huntr.co/) to manage the “money-back” guarantee students, etc.), where the stakeholders would turn to MVP / no-code / external vendor approach to build a solution that fit their needs. This way, they have 100% control over what they are doing and are not blocked by Engineering (limited) resource allocation. It’s a great way to explore the product bounds and figure out what needs to be built. And in the end, with the no-code product in place, it can be shown to Engineering to be built again with more robust / scalable / long-term approach if it outgrows that first solution.
A bird’s eye view of what is needed seems to be:
1. A form to collect information about a teacher (Google Form + Spreadsheet)
1. An e-signature tool compliant with German law (User access to Docusign, like Legal, HR and B2U. [Docusign supports QES](https://www.docusign.com/products/electronic-signature/legality/germany), I’d recommend we set up a **new account** for it to have 100% control on settings. *💡 **The constraint that the contract can only be sent if all the days are known in advance is the final nail in the coffin in the current Kitt implementation. This is not a “small change”, it’s a whole rewrite (that we won’t do). Hence the nocode approach with Google Workspace software suite + DocuSign.*
1. Extract of Batch calendars with hours (we can set up a **Connected Sheet** on the Datalake to expose the Batch calendars of german cities)
We then can **turn off **the creation of Minijobbers Contracts and Extensions in Kitt, and staff these people as **employees **when adding them to a batch crew.
Based on those assumptions, Engineering can also work on additional Connected Sheets to help German HR team make sure every minijobber added is in check. We also recommend that German HR team sets up a process for Batch Managers to follow to help them comply with the German law. Again, the solution is not code, it’s efficient process and a way to **enforce **it long-term.
## Related
- [[Content]]
- [[MiniJobbers]]

---
type: notion-import
notion-id: d5c596c409b246f69a5c4e255916cdc2
source-url: https://app.notion.com/p/lewagon/Hubspot-x-WhatsApp-d5c596c409b246f69a5c4e255916cdc2
imported: 2026-07-23
---
# Hubspot x WhatsApp
## Context
In 2020, a first effort to introduce some Sales practise in the Admissions team was done and embodied as a feature in kitt called “Hubspot Leads” (/cities/:slug/hubspot_leads) which was consuming a www API to retrieve leads for a given course, program format and city:
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F46d7682d-0094-445a-91a2-dfa7f4021ed5%2FScreenshot_2022-10-10_at_14.18.43.png?table=block&id=b40d35d2-e9cf-48dd-a2ee-059be16fd705&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=540&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ffd7abfcb-3e65-4289-97c5-4db072401255%2FUntitled.png?table=block&id=b222ab32-70c6-465f-a019-149246aa16e5&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=560&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fffada8fe-d9e2-404c-b9d0-eb78343e0d75%2FUntitled.png?table=block&id=d85bf876-c0db-4210-8be8-5efefa00498d&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=730&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
This features creates a coupling between www and kitt, makes us dependant on a Hubspot [deprecated](https://developers.hubspot.com/docs/api/deprecated-apis) API and requires constant configuration maintenance to keep the list **ids** up to date.
Hubspot is *already* a good Sales CRM and can log any interaction with a lead (meeting, call, text message, etc.) with a good CRUD UI for that job to be done. No need for us to put Kitt in the middle of that!
To pay some technical debt, Engineering has decided to **sunset **🌆 the Hubspot Lead feature in Kitt. After some investigation, it turns out the “Call” button which opened a [wa.me/](http://wa.me/) URL (WhatsApp) was quite used, and is missing from Hubspot. To mitigate that loss, we have extended the attribution of the [[../Product Wiki/Chrome Extension]] , only used so far for Linkedin Scraping. That’s a good middle ground solution where we don’t implement non-core business features in Kitt but still deliver value to Staff by enhancing the behavior of their favorite tools. That’s a pattern we will surely reuse in the future for Product Development.
## I want to initiate WhatsApp texts from Hubspot!
Here’s what you need to do: download the latest version Zip and follow the [[Chrome Extension|instructions]]:
> [!warning] Database view not exported
> [[Releases]]
Once installed, you can check that the extension is working by navigating to a Contact page (one with a phone number), and click on “Log a WhatsApp message” orange button at the top-right (it will be in the dropdown, don’t hesitate to **re-order** those icons to the ones you use the most).
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F29485393-7ef5-46b6-a304-82c329ed6c65%2FScreenshot_2022-10-10_at_11.58.20.png?table=block&id=004e79b2-4060-4e61-a053-26063bf358a7&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F70707789-b308-464a-bf5c-6f39a6f863ce%2FUntitled.png?table=block&id=799ea22e-5aa4-45c9-9de1-c3454f2a75c3&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F0801bb22-92c1-4a70-aa70-82d368a69a5d%2FUntitled.png?table=block&id=4a9db5f5-e80c-4798-b743-b7529928bfdc&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F467a7c1b-f728-48b4-9c19-8f5a9f878d16%2FScreenshot_2022-10-10_at_12.19.01.png?table=block&id=d376a473-33c3-4299-af14-c180a5082007&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Faee4b910-88e2-4da8-b5e2-504e141aa36e%2FScreenshot_2022-10-10_at_23.51.19.png?table=block&id=5c890410-f5dd-428f-9373-8ea56d952c37&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F547e9ddd-f449-4878-b1f6-02d3bfe859a5%2FScreenshot_2022-10-10_at_23.51.16.png?table=block&id=d9449544-61a8-4255-b2c5-2c4104967a89&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Follow-up
This release is intentionally minimal to clear the technical debt as soon as possible. Engineering expects Sales & Admissions to install / update the extension and start using to provide feedback in the context of [No access](https://app.notion.com/p/2d685f2cff45451e92d63e2ad9039523?pvs=24#2d685f2cff45451e92d63e2ad9039523) ‘s mission topic. That’s why **message templates** are not part of this release, also it appears that the Desktop App supports a Templating feature.
## Related
- [[Chrome Extension]]

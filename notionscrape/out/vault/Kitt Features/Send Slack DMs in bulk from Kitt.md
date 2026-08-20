---
type: notion-import
notion-id: 1928924af0148029997acfd4e1402bba
source-url: https://app.notion.com/p/lewagon/Send-Slack-DMs-in-bulk-from-Kitt-1928924af0148029997acfd4e1402bba
imported: 2026-07-23
---
# Send Slack DMs in bulk from Kitt
## Context
The Operations and Finance team frequently have to send reminders via Slack, but manually drafting and sending messages individually is time-consuming.
## Solution
We introduced a **Bulk Slack Messaging Form**, making it easy to send reminders to multiple students at once.
The feature will be accessible in the Global section of the sidebar
> [!note] 
> This feature is currently in beta testing and available to a limited group of users, with accessibility gradually expanding over time.
![](https://app.notion.com/image/attachment%3Ab45ef793-ba38-4155-8efe-e98aa8fd54d3%3ACapture_decran_2025-02-18_a_14.49.09.png?table=block&id=19d8924a-f014-80c3-999a-c59149915a05&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
**This form provides several key features :**
- **Selecting Recipients**: Add recipients by entering or pasting multiple email addresses. Users can either copy and paste a list of comma-separated emails or directly use a column from a spreadsheet. Valid associations are marked green, while invalid ones are marked red.
![](https://app.notion.com/image/attachment%3Aeb1d928c-def6-47cc-be5b-66e9868a2f4d%3ACapture_decran_2025-02-18_a_16.05.01.png?table=block&id=19e8924a-f014-80e1-a009-de8e8e5558c1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
- **Sender Selection**: Users can choose to send messages either from **themselves** or **KittBot** depending on their needs.
> [!note] 
> If your Slack alumni account is not linked to your Kitt account, the notification will be sent by Kittbot.
- **Template Management**: Users can select a **predefined message template**, which automatically loads into the message editor. You can request new templates or updates of an existing template here 👉 [[../Product Wiki/Bulk Slack templates]]
![](https://app.notion.com/image/attachment%3A640485ae-b6b5-4a4a-a3a7-442fa672ea0f%3ACapture_decran_2025-02-17_a_18.13.58.png?table=block&id=19e8924a-f014-8031-ac87-c8e1433e5d5b&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
- **Dynamic Variables**: Messages support **dynamic variables**, allowing bulk personalised content.
![](https://app.notion.com/image/attachment%3A7238b060-0643-4dcd-bf5e-4b09a2a339fd%3ACapture_decran_2025-02-18_a_16.06.12.png?table=block&id=19d8924a-f014-809d-9002-e2abbb16a589&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related
- [[Bulk Slack templates]]
- [[Content]]

---
type: notion-import
notion-id: 65495301092a490daf05ed13bad8add0
source-url: https://app.notion.com/p/lewagon/Calendly-Setup-Guide-65495301092a490daf05ed13bad8add0
imported: 2026-07-23
---
# Calendly - Setup & Guide
> [!note] 
> Calendly is used as our **go-to scheduling tool** to share with leads that want to book a call with the sales team. All #core sales associates or team members that have recurring 1to1 contact with leads should use Calendly.
**🕧 Last updated: 29.03.2023**
## Version Log ⚙️​
*Any changes done on global workflows or important releases*
---
Version​Date​Changes TL;DR​V4.029.03.2023- Updated email reminder 24 hours before that includes a “re-confirm” button so that we can better predict attendance to calls;
- Updated SMS workflows with new copy;
- New email that is sent the minute the event is scheduled to start saying that the event is happening with the link to access;
- Google Meet as the standard location for every call;
- Events will have an updated title: It will be “Call with Le Wagon’s Advisors - UK” (e.g. for region name) and standardized URL;
- There will be a new question to ask leads to write down their city of interest: to allocate leads on HubSpot and assign sales owner;
- Country-specific phone numbers will send the SMSs instead of the generic US number used for all leads currentlyV3.028.02.2023- Copy and questions equal across all Calendlys
- Routing forms created to be shared globally as a single CTA that directs to the right scheduling meeting
- Automated SMS from local number and stabilized workflow 
- Full integration with HubSpotV2.028.09.2022- Automated email and SMS workflow to remind leads of meetings
- Automated additional reminders when leads book calls with >10 days in advance
- Confirmation page after booking a call with new CTAs (Workshops; Financing; Outcomes Report)
- Updated Le Wagon Branding instead of Calendly brandingV1.001.03.2022- Calendly implementation and testing across teams
## Sales Calendar Links per Country 🏴‍☠️​
---
## 0. Why use Calendly? 🤔​
---
We moved from Hubspot to Calendly, as it allowed for 4 main features:
- **Round robin: **The possibility to have multiple owners of an event that are assigned based on availability - critical for regional teams that have more than 1 team member doing sales. One link is enough now, that is connected with multiple calendars and does an automatic rotation;
- **Automated SMS & Email: **To decrease no-shows, it allowed to have an automated flow of both SMS and emails that is Le Wagon branded and with copy that we can choose;
- **More flexibility in new events / event changes: **If hosting an open-campus event, campus tours, a 15-minute call as part of a campaign, etc. calendly allows for easy creation of new events;
- **Routing forms: **Possible to have a single link that directs to the right meeting link depending on the leads interest - important for the website / global posts / etc.
## 1. How to setup Calendly 📅​
---
Log-in to [Calendly](https://calendly.com/login) with your LW address. The majority of the setup will already be done for you, so you just need to setup two quick items 🤞​
**Setup **[Integrations](https://calendly.com/integrations)** & Location**
To make sure you can access video conferencing apps, go to [integrations](https://calendly.com/integrations) and log-in with:
- Zoom
- Google Meet
***Note: ***Preferably, you should use Google Meet only, as it’s easier for leads to join as they don’t need to download an app
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F58cb8e0a-8a80-41e3-b0ca-8c10674ed373%2FCaptura_de_ecra_2022-09-27_as_17.47.03.png?table=block&id=e40be032-c120-4001-ba0e-6160e44d38ed&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
**Setup Availability**
So that your schedules work based on your availability for calls, add your availability per day and per hour.
This availability will automatically reflect on your regions sales calendar!
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F9853debd-78d6-4d18-8019-e2985439ac8b%2FCaptura_de_ecra_2022-09-27_as_17.47.31.png?table=block&id=2bd2afe6-171d-4e4b-bee4-be19f1ce73ed&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
ℹ️** Info: If you’re OFO or need to block slots**
- On availability, go to “[Data Overrides](https://calendly.com/app/availability/schedules)” and add a data override
- This will block your calendar on calendly for the dates you chose, not offering those slots
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6f885005-2fb4-48a3-8115-0b4250c2c41f%2FCaptura_de_ecra_2022-09-27_as_17.55.23.png?table=block&id=cc4968f9-e95a-4b1d-8bd4-c16022b6480d&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
This is a pretty quick setup, as all automated workflows and settings have been already defined! If you want to know what’s being sent to leads and how, check below ⤵️​
## 2. What happens when a lead books a call 🕞​
---
### Scheduling a call 📞​
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F9d1e1af4-a670-4b1d-9094-d7631026689a%2FCaptura_de_ecra_2022-09-27_as_18.03.56.png?table=block&id=17d45d95-e9aa-4b6d-a89b-199fef1a01ae&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
- [This](https://calendly.com/d/d69-pcc-86x/call-with-region-s-admissions-specialists-template?month=2022-09) registration page is the one our leads will see to book a call with us.
- It has a simple description of what they can discuss on the call and balances expectations
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F9661cabd-8186-487a-b7a2-a21cc73fd8e9%2FCaptura_de_ecra_2022-09-27_as_18.04.29.png?table=block&id=219c2822-f058-4a1a-a06a-47210fe6311c&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
- When submitting their contact request, leads will be asked for their phone number and email.
- Optionally, they can say which bootcamp they are interested in and if they can already write down some questions. This can help prepare the meeting
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc9b9ecf1-87f2-4c82-952d-87c75548d4c9%2FCaptura_de_ecra_2022-09-29_as_08.35.45.png?table=block&id=1aa932ef-30f6-429a-a469-3551cf94fe36&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
- After booking the call, the confirmation screen shows the link for 🤑 **Financing** **Options**; **🤝 Outcomes Report**, and; 💻 **Workshops**; as to have another CTA for leads as they are waiting for the call
### 2.1 Automated Reminders 💬​
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3cbc725d-283b-4dca-ae64-f8105a082369%2FUntitled.png?table=block&id=d4a384c8-55eb-40bf-a401-282f52fb9cb1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Reminders follow the pattern above to make sure we **decrease the % of No-Shows**:
- **10 days before, **a special email reminder is sent, and is meant for leads that book a call far in advance and might have forgotten about it;
- **24 hours before**, they receive a simple email reminder with the google meet / zoom link and a button to reconfirm their presence;
- **1 hour before,** they receive both a simple reminder by both email and SMS as a final call to join the link on time before the call;
- 🆕 **As the call is starting, **they receive an email with the link and the possibility to reschedule if attending was not possible;
## Related
- [[Events]]
- [[Releases]]

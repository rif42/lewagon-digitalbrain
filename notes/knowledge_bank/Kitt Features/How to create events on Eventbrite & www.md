---
type: notion-import
notion-id: 8fe689b201c3435b944c2bf7570b0d77
source-url: https://app.notion.com/p/lewagon/How-to-create-events-on-Eventbrite-www-8fe689b201c3435b944c2bf7570b0d77
imported: 2026-07-23
---
# How to create events on Eventbrite & www
The old event creation form in the legacy admin has now been terminated 🌇.
We have introduced a **new Eventbrite integration** to leverage Eventbrite’s event form capabilities and still being able to publish events on our city pages (on www).
This feature is very close to the legacy one:
- Events are displayed on the city page and on Eventbrite
- Registration forms on Eventbrite have a set of marketing questions to qualify the leads
- Attendees registration data is pushed to Hubspot
But it changes one thing:
- **Events are created directly in your city’s Eventbrite account **
- No more event creation directly in www's admin
> [!note] 
> Pre-requisites: You must have set up your Eventbrite account with your city in www’s admin - [[How to link your Eventbrite token to your city|This tutorial explains how to set it up properly.]]
## 1. Event creation on Eventbrite
### Basic info
On your city’s Eventbrite account, simply **create your event**, adding a name, tags and location.
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F6b189574-906b-4cbe-95a3-2d9c2b048956%2FUntitled.png?table=block&id=4961c297-1e52-49ab-b05a-6c3b44edea4d&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F375bf883-fd6f-42ea-9e74-d3ba80691c70%2FUntitled.png?table=block&id=d389d5a2-65e6-4a1d-92cf-6d84a40c6640&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### Location
The **venue** you link to your event on Eventbrite will be displayed on the event card on www.
If you’re event is happening online, you can also select Online Event .
### Date & Time
Make sure to select the right dates and the relevant timezone.
### Details
In the next page, add some pictures and the relevant description and summary.
### Tickets
Once done with the Details, create your tickets for the event
---
### Publication
Finally, **publish the event.**
> [!note] 
> While all the pieces of informations and details are important for your event, only a subset of these will be displayed on www :
- **name**
- **venue address** and **name** (or Online )
- date and time
The rest (cover picture/video, description, summary…) will only be displayed on the event’s Eventbrite page (where attendees ultimately land to register)
### Registration forms (question)
Our integration between www and Eventbrite will make sure your newly created events have the proper questions in the registrations forms (phone, job title, company, and also some marketing questions). You should not have to take care of this, these questions will be added **automatically.**
If you want, you can check in Order Options > Order Form that the **default and custom questions **that will be asked to attendees have indeed been added to the event ✅​
<details><summary>Screenshots 👇​</summary>
</details>
These will be the questions asked to attendees when they sign up to the event, and their answers will be eventually forwarded to Hubspot.
## 2. Events on www
> [!note] 
> When the event is created on Eventbrite, www gets notified and create a new event record in its own database
Once your event has been created on Eventbrite, you can go to:
- the **Local events page **on [lewagon.com/v4/admin/resources/local_events](http://lewagon.com/v4/admin/resources/local_events)
- or **on your city’s admin page in the tab **Local events**.**
Our event is already there 🎊 and is filled with its :
- name
- dates
- venue information
> [!note] 
> By default, newly created events on www are not “**published**”. You have to publish them yourself.
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1eb53c57-7a96-49cf-89a4-4f674b251dc1%2Fevent1.png?table=block&id=b22f03ec-e86f-4794-a3e3-858879f51749&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1440&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fbba4e083-dbee-4ade-a76a-67d831df9d05%2Fevent2.png?table=block&id=3fa2223d-dc21-4424-9e20-37b2b0c94a18&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1440&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Open the Event on www, make sure that the **timezone **is the right one (otherwise update the event) and click on the button at the top-right to **Publish** it:
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F803dff26-a28a-44cd-b828-31ebf01687f9%2Fevent6.png?table=block&id=32f884a1-ea35-4daa-99f9-40655e27b4fa&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
It is now displayed on your local city page 👇​
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F793725d4-d801-47d3-bbb6-e9be2c9e2612%2FUntitled.png?table=block&id=39f88991-5c1b-469e-83e5-a66330fe18bb&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## 3. Connection with Hubspot
> [!note] 
> Nothing has changed here. The connection between Hubspot and Eventbrite behaves the same way
Every time a prospect will sign up to your event, they will have to fill in this form, on top of their contact details:
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F16fa20f1-ab22-4eac-9696-d829ea870bed%2FUntitled.png?table=block&id=72f5759b-1ad0-4203-8588-7f226e08cbc5&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
As usual, these information will then be sent to Hubspot when they submit their attendance form on Eventbrite.
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F05ea925c-5c76-402c-9f35-39f2953ce640%2FUntitled.png?table=block&id=887e0cec-203f-44c0-9133-db5a0a46a419&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Voilà 🎉​
## 4. Event management & filters
You can manage your events on www from:
- the **Local events page **on [lewagon.com/v4/admin/resources/local_events](http://lewagon.com/v4/admin/resources/local_events)
- or **on your city’s admin page in the tab **Local events**.**
You can use the **Filters**** **to easily find local events:
- for your city
- In person / Online
- Upcoming / Past
- Created on Eventbrite or manually on www (if you don’t need to create it on Eventbrite or if you have created it on another platform)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F97c1175c-767d-4fdf-aac2-2442bd8cf943%2Feventfilter.png?table=block&id=5905e019-833f-4460-8e28-e20ce17a2d3f&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related
- [[Events]]

---
type: notion-import
notion-id: 3768924af0148014a334c6f4eec1a168
source-url: https://app.notion.com/p/lewagon/Sending-SMS-through-Brevo-3768924af0148014a334c6f4eec1a168
imported: 2026-07-23
---
# Sending SMS through Brevo
*last updated by Diana Baleya **@June 5, 2026** *
> [!note] 
> **useful links**
SMS marketing campaigns are sent from **Brevo**, but the audience should first be prepared in **HubSpot**. Before importing contacts into Brevo, make sure the list includes the correct mobile phone numbers with the proper **international country codes**.
This is essential because Brevo needs phone numbers to be formatted correctly in order to deliver SMS messages & to avoid wasting our credits = budget.
The general workflow is:
1. Create the target contact list in HubSpot.
1. Make sure phone numbers include the correct country code.
1. Export the list from HubSpot.
1. Login in to Brevo with details in Bitwarden
1. Import the list into Brevo.
1. Create the SMS campaign in Brevo.
1. Select the exact imported list as the recipient list.
1. Test the SMS before sending.
1. Schedule or send the campaign.
## **Step 1: Create the Contact List in HubSpot**
Start by creating the audience list in **HubSpot**. This list should include only the contacts who should receive the SMS campaign.
When building the list, check that each contact has a valid phone number. The phone number must include the correct **country code**, for example:
- France: +33
- United Kingdom: +44
- Spain: +34
- Germany: +49 (but we have no tested SMS to germany due to GDPR)
This step is very important. If phone numbers are missing the country code or are formatted incorrectly, the SMS may fail to send.
### **Things to check in HubSpot**
Before exporting the list, review the following:
- The list contains the correct target audience.
- Each contact has a mobile phone number.
- Phone numbers include the international country code.
- You have excluded alumni, people in in pipe, etc (if applicable)
- Contacts are eligible to receive marketing communications.
- The list name is clear and campaign-specific.
Recommended naming convention:
```
SMS - [Campaign Name] - [Country/Region] - [Date]​
```
## **Step 2: Export the List from HubSpot**
Usually I select CSV format, you will see it in your email and browser.
## **Step 3: Import the List into Brevo**
first, you have to create a lsit to improt your contacts into, use the same name as you used in HS, and add it to a folder (you may have to create one)
![](https://app.notion.com/image/attachment%3Ae5d43b1d-f3bf-4068-92dd-1ac943960aa1%3AScreenshot_2026-06-05_at_1.10.57_PM.png?table=block&id=3768924a-f014-8073-b0ea-db094dc7d827&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
then you go to Contacts tab, click import contacts, then click Contacts box and Continue.
![](https://app.notion.com/image/attachment%3A804c55f3-5d61-46c1-a833-d147cf90097b%3AScreenshot_2026-06-05_at_1.12.46_PM.png?table=block&id=3768924a-f014-80d8-af19-e965ca729bf6&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Choose** Import contacts from a file **and then follow all the steps you see below: Upload file (your HS list), Map data, and then you select the List you created 2 Steps ago in Brevo.
![](https://app.notion.com/image/attachment%3A420155ec-88ab-4699-b149-4978ef5d240b%3AScreenshot_2026-06-05_at_1.13.32_PM.png?table=block&id=3768924a-f014-80dd-89cb-db81eac4ccc7&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
When importing, make sure the phone number field from HubSpot is mapped to the correct SMS/mobile phone field in Brevo.
If Brevo asks you to confirm column mapping, carefully check that:
- The mobile phone number column is mapped to the SMS phone number field.
- Phone numbers include country codes.
- The list is imported into a clearly named Brevo list.
- The list name matches the campaign or HubSpot export name.
Recommended Brevo list naming convention:
```
SMS - [Campaign Name] - [Country/Region] - [Date]​
```
Use the same or nearly the same name as the HubSpot list to avoid confusion.
## **Step 4: Create the SMS Campaign in Brevo**
In Brevo, create a new SMS campaign.
![](https://app.notion.com/image/attachment%3A3cad54df-403c-4e83-a18a-8f201ffe8254%3AScreenshot_2026-06-05_at_1.16.23_PM.png?table=block&id=3768924a-f014-8094-b63d-fddf8002eaa1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Add the SMS content carefully. Keep the message short, clear, and action-oriented. Remember that SMS messages have character limits, and longer messages may be split into multiple SMS credits.
A typical SMS should include:
- The main message or reminder.
- A clear call to action.
- **I****mportant:**** **A short link if needed. —> i use <https://lew.ag/> (before you create this link make sure you create a tracking URL in [Hubspot Campaigns](https://app.hubspot.com/marketing/4419217/campaigns/views/35783442) - you maybe have to do it in an existing campaign or create a new one) If you don’t do this you will not be able to track perf from your SMS campaigns inside Hubspot
- The sender identity if it is not obvious.
- Opt-out wording if required by local regulations. → [STOP] (you can see examples inside previous SMS sent in Brevo)
Under **Sender name we put “Le Wagon”**
![](https://app.notion.com/image/attachment%3Ad7dc32d1-934a-47cf-bebe-7bedd78748e3%3AScreenshot_2026-06-05_at_1.20.21_PM.png?table=block&id=3768924a-f014-8052-becc-e98c15ddfa9e&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## **Step 5: Select the Exact Imported List**
When choosing recipients in Brevo, select the **exact list** that was imported for this campaign.
This is one of the most important steps. Do not select a similar-looking list or an old version of the list. Always double-check the list name, date, and audience size before continuing.
Before moving forward, confirm:
- The selected list is the one exported from HubSpot for this campaign.
- The list name matches the campaign.
- The number of contacts looks correct.
- The list is not outdated.
- No unrelated audience has been selected.
![](https://app.notion.com/image/attachment%3Aac14d6a6-8897-4463-95c7-f75143168685%3AScreenshot_2026-06-05_at_1.21.40_PM.png?table=block&id=3768924a-f014-80cf-afdd-f96b6c07b3bc&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## **Step 6: Test the SMS Every Time**
Always send a test SMS before scheduling or launching the campaign.
This should be done every single time, even if the campaign is similar to a previous one.
When testing, check:
- The SMS is received successfully.
- The sender name/number appears correctly.
- The message is clear and free of typos.
- Personalization fields display correctly.
- **Links work on mobile.**
- **The link goes to the correct page.**
- The message is not too long. (under 160 characters total otherwise you pay double/triple)
- The opt-out text, if included, is correct.
- The final recipient list is correct.
![](https://app.notion.com/image/attachment%3A0a3397da-9f18-4746-8bc5-a872b67fcb16%3AScreenshot_2026-06-05_at_1.25.54_PM.png?table=block&id=3768924a-f014-8043-b896-db21823b202d&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=540&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
If anything looks wrong, fix it and test again.
## **Step 7: Schedule or Send the Campaign**
Once the SMS has been tested and everything looks correct, schedule or send the campaign.
Before the final send, do one last review:
- Correct recipient list selected.
- Correct phone number formatting.
- Correct SMS copy.
- Correct links.
- Correct send date and time.
- Campaign approved internally, if required.
If scheduling the campaign, make sure the selected time zone is correct.
## **Final Checklist**
Before sending any SMS campaign, confirm the following:
CheckHubSpot list created with the correct audiencePhone numbers include international country codesHubSpot list exportedList imported into BrevoPhone number field correctly mapped in BrevoBrevo list name is clear and campaign-specificSMS campaign createdExact imported list selectedTest SMS sentTest received and reviewedLinks checked on mobileFinal audience and send time reviewedCampaign scheduled or sent
## Related
- [[Audience]]
- [[Campaigns]]
- [[Content]]
- [[Diana Baleya]]

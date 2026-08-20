---
type: notion-import
notion-id: 1838924af01480079393e83d37aa655d
source-url: https://app.notion.com/p/lewagon/How-to-create-and-use-forms-1838924af01480079393e83d37aa655d
imported: 2026-07-23
---
# How to create and use forms ?
<!-- unhandled: transclusion_reference -->
No accessYou don’t have access to this synced blockRequest access
> Note that if you want to create a Syllabus form you can skip these steps and follow this guide [No access](https://app.notion.com/p/187ebdb1d22b4db58f6400eaf16684a3?pvs=24#187ebdb1d22b4db58f6400eaf16684a3)
---
# 🦧 Using Hubspot
<!-- unhandled: transclusion_reference -->
No accessYou don’t have access to this synced blockRequest access
### ⚠️ The mandatory proprieties’ usage
Whenever you are creating a form, you **must **have the following proprieties in your form 👇🏻​
- **First and Last name**, they are mandatory for creating or updating the Contact object
- **Email**, this one is mandatory for HubSpot to create/update the lead
- **Touchpoints**, you need to choose the correct value based on where do you will place the form [Hidden Field]
- **Lead type**, should in 99% of the use cases set as B2C [Hidden Field]
- **Smart Rules - Preferred Language**, if your campaign is not worldwide you need to set these value to the lead language [Hidden Field]
- **utm_campaign**
- **utm_content**
- **utm_medium**
- **utm_source**
- **utm_term**
---
These are a must-have to ensure that we are not losing any tracking data [Hidden Field]
- **Smart Rules - Preferred Language**, if your campaign is not worldwide you need to set these value to the lead language [Hidden Field]
- Always keep one legal text mention **non-checked & non set as required field **
> [!note] 
> If you need to mention a specific Campus, use the propriety **Campus **and add a conditional logic to ask **Country **if the **Campus = Online**
## ⚠️ Mandatory proprieties in some specific uses cases
### For European countries the GDPR is **mandatory **, you can find the correct text 👇🏻​
### Want to collect information about courses? 📔​
### Need to collect phone numbers ? ☎️
> [!note] 
> Please **never **create the simple workflows displayed by Hubspot in the Automation section.
If you need to have any actions to the leads that submitted your form *add to a list, send an email , * ask the @Baptiste Derenne or @Andrey Bondaryev
## 🔨 The Building process
### The basics
You have the choice between taking a form that is similar to the one you want to build and adapt it, or create your own from scratch, let’s see together the steps 👇🏻​
*If you are creating a new form,*
1. For the moment, always use the **Legacy Form Builder**
1. Start with a Blank Template
### Edits
1. On the left side you are seeing all the proprieties where you can store the answers to the questions
1. When you click on a field, you can see new options for each question
    ![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F8f4f57de-eb12-418f-b2cf-deec3414f7bc%2Fimage.png?table=block&id=19d8924a-f014-81f4-99f3-e8647d4bf118&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=600&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
        1. Label : The name that will be displayed for the contact, **translate it to your language**
        1. Help text: A quick sentence to explain the purpose of this field, if needed
        1. Placeholder text : The gray text that serve as an example in the field
        1. You can also set a default value, **if you do so the Placeholder text will be deleted** !
    ---
    For the dropdown proprieties as campus you will have different customizations possibilities
    ![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F4fabf12d-ef88-4a37-bcc7-8d08c2670d77%2Fimage_2024-09-19_142505046.png?table=block&id=19d8924a-f014-8116-b5d1-fc62318fc90b&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=670&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
        1. You can preselect a value **mandatory for **[Hidden Field]
        1. If you click on the blue pen 🖊️, you can change the displayed value as in the example, the lead will see *I am not Bali* but the value set within the CRM will be bali
        1. If you click on remove, you are able to reduce the number of choices offered to your lead
---
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fd6540933-346f-4af2-8214-d1134c24a737%2Fimage.png?table=block&id=19d8924a-f014-8124-878c-d37922e6381c&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=390&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
---
### The building and the post building part
1. Use the search bar to add the **mandatory proprieties **and the one that you need for your purpose, you need also to decide which ones are **required fields, **optional and [Hidden Field]
1. Once your form looks great, you can go to the **Options **tab,
        1. **Always **change the displayed message after submitting from Text to HubSpot Page or External URL
        💡 If you search for “**thank”, **you** **will find a list of premade pages that may correspond to you !
            ![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F2b9d5c0a-55a7-434f-813e-a5e7b29ad730%2Fimage.png?table=block&id=19d8924a-f014-81e4-a204-ed684d9a1279&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=840&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
        1. **If you know what you are doing** you can change the Lifecycle Stage, otherwise keep it as Default our Workflow’s will set the correct Stage for you !
            ![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Ff6e68852-b992-4417-bf83-227d7eb23483%2Fimage.png?table=block&id=19d8924a-f014-81d6-b2be-e2f8b3e4049d&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=830&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
        1. You can send yourself some notifications for each submission
            ![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Ffc2b1355-14fa-430d-8178-64e40dcbd2f4%2Fimage.png?table=block&id=19d8924a-f014-8150-aa67-f536eac46779&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=870&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
        1. Set the Error message language to the same value as **Preferred Language**** **or keep it in English if non-existent ** **
            ![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fb78365a2-4e15-48cc-a346-f9664d4f2a30%2Fimage.png?table=block&id=19d8924a-f014-8144-9daf-d99020333010&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=850&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
        1. Here you can add your form to some specific campaigns to keep a track
            ![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F0de58b28-d697-4693-b32e-66176222a552%2Fimage.png?table=block&id=19d8924a-f014-81da-abd0-ddc5df0cc9d5&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1220&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
            > [!note] 
            > Some Wagoners encounter errors in form submissions in a specific case.
            If a lot of people will submit the same form on the same computer, you need to turn ON **Always create contact for new email address**
            ---
            ### The specific field types
    The purpose of the [Hidden Field] is to prepopulate some values for each submission without the lead need to make any action on his side, to set a field as [Hidden Field] you need to
        - Click on the field
        - On the left pane activate make this field hidden
    > A field can’t be [Hidden Field] and **required **! So choose wisely 🧙🏻‍♀️​
    The conditional logic is accessed by clicking on the **Logic **tab
    ![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fdc81a273-23c9-4f85-b459-a359c1d68d78%2Fimage.png?table=block&id=19d8924a-f014-819a-8042-da9c11629269&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=600&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
    ---
    1. You need to choose a logical test
                    1. Containing x value
                    1. Not containing x value
                    1. Empty 👈🏻 This one is mostly for CRM part
        1. Choose the value on which you want to do your logical test
        1. Decide which other question should appear if your logical test succeed
    ---
    > [!note] 
    > Please, **never **create the Simple workflows displayed by Hubspot in the Automation part.
    If you need to have any actions to the leads that submitted your form *add to a list, send an email * ask the @Baptiste Derenne or me, @Andrey Bondaryev
## 🍋 Using Typeform
> In some rare cases you will need to create a Typeform form, so let’s review how this plateform is working
> ⚠️ Note that before starting building your typeform you need to reach someone from the CRM Team to be sure that the goal you want to achieve and the data collected can be fit in the CRM
On the Typeform UI you will see the different groups, called Workspaces.
1. Choose first the group where your form belong, or create your own
1. Click on create a new form
---
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F8351d578-7667-4d91-ab18-07fe4d36dab6%2Fimage.png?table=block&id=19d8924a-f014-8169-8485-f8427eae1dc8&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=260&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
On the building page, you are able to create your form from scratch or import a Google Form.
If you select create from scratch, you will see a full list of questions that you can prompt to the lead.
The form building is pretty simple, you just have to keep in mind that the questions you are asking should fit in the HubSpot proprieties.
On the left pane of the Typeform UI, you are able to switch to two other tabs
- Design, here you can choose a premade Le Wagon design and apply it to the entire form
- Logic, as in the HubSpot form, you are able to create logic tests to redirect the lead to different question based on his answers
Once your Typeform built you can publish it, and you can share it via the “Share” tab and see the results within the “Results” one.
---
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2Fc518cdb6-dca0-485a-a8cd-f0f6df56cf9b%2Fimage.png?table=block&id=19d8924a-f014-81c5-a519-d754439909dd&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=560&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F33992dce-3dad-4eca-8a95-6d0b8dec46cb%2Fimage.png?table=block&id=19d8924a-f014-8108-8601-e37898d93af3&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!note] 
> Please, **do not try**** **to connect the Typeform to HubSpot by yourself ask @Baptiste Derenne or me to connect it.
## Related
- [[Baptiste Derenne]]
- [[Campaigns]]
- [[Content]]

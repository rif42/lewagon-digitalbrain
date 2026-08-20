---
type: notion-import
notion-id: 1a78924af0148006b805ff130f695bb6
source-url: https://app.notion.com/p/lewagon/Setting-Up-a-Partnership-with-revenue-compensation-in-the-CRM-1a78924af0148006b805ff130f695bb6
imported: 2026-07-23
---
# Setting Up a Partnership (with revenue compensation) in the CRM
*Last edited: **@March 1, 2025** *
> [!note] 
> **Introduction to Setting Up a Partnership in Your CRM**
# Step 1 - **Duplicate the Template Landing Page and Customize It**
To kickstart your partnership setup, you’ll need to create a dedicated landing page. We’ve provided a **template landing page** designed for a partnership with Malt. Follow these steps to duplicate and personalize it:
1. **Access the Template** – Click on the link below to open the template landing page:
    👉 [HubSpot Landing Page Editor](https://app.hubspot.com/pages/4419217/editor/182922699537/content)
1. **Duplicate the Page** – In the HubSpot editor, locate the **"More"** options and select **"Clone"** to create a copy of the template.
1. **Customize the Content** – Update the page with your partner's branding:
        - Replace text to match your specific partnership.
        - Adapt sections to align with your messaging.
        - Change the logo to reflect your partner’s brand.
1. **Edit the URL** – Ensure the landing page has a relevant, clean URL.
    <details><summary>*How to Edit the URL of a HubSpot Landing Page*</summary>
    </details>
---
# Step 2- **Add the main UTM Term value & source**
To ensure accurate tracking of leads and conversions, you need to add every time the partner name in the URL thought UTM term parameter & source (not utM_source, read this [[Apply with Source in URL|doc]] ) OR in the CRM (if specific partner like Malt which have specific conditions). Follow these steps to get it done:
1. **Create a GitHub Request (if partner similar to Malt with several conditions)** – Submit a request to the CRM team via GitHub, asking them to add the new partner (or influencer) to the system.
1. **Include UTM Term Details** – Specify the **UTM term** you’ll be using to track this partner.
1. **Define the Source Parameter** – Determine the **source value** that will be included in the URL of the apply form, especially if the link will be shared via email.
### **Example Configuration:**
- **UTM Term** → utm_term=malt
- **Source Parameter** → source=malt WARNING, it’s not utm_source
🔗 **Example Apply Form URL:**
lewagon.com/apply?source=malt
📌 **Why This Matters?**
These parameters are essential for **precise lead attribution**, allowing you to track which partners generate the most engagement and conversions. We will adapt our workflow inside or use it for the dashboard where you can select your partner name.
---
# Step 3 - Select the form to generate leads and more
> [!note] 
> As you know, there is different way to generate leads, especially different approach. Our goal is to cover the main approach you can set up. So, based on your intention, select one of these options and follow the guidelines,.
## Option 1 - Create and Integrate Your Embedded Apply Form
## Option 2 - **Add the "Claim Discount" Form (or Use It as Another Form)**
## Option 3 - **Leverage the Syllabus Form to Capture Leads from Partner Channels**
## Option 4 - no form, only link to redirect to our website or Landing Page
---
# Step 4- Share the Tracking Link with Your Partner or Influencer
Now that your tracking link is ready, it's time to **share it with your partner or influencer**. To ensure accurate tracking, they **must** use the correct UTM parameters.
---
> [!note] 
> **🔑 Key Rules for Sharing the Link Correctly**
**Create a Short Link for Easy Sharing**
To make the tracking link more user-friendly, shorten it before sharing:
👉 **Go to **[Lew.ag](https://lew.ag/)** and create a short link.**
📌 **Example:** lew.ag/partnershortlink
🚀 **Now, share this final short link with your partner/influencer and start tracking leads!**
> [!note] 
> **Important Documentation:
**
🔴 **Reminder:** Ensure your partner **only shares the correct, UTM-tagged link** to track all leads effectively! Test it before
---
# Step 4- **Tracking Your Influencer/Partner Campaign Performance**
> [!note] 
> Message from Baptiste: We are currently working on the dashboard to get accurate data. we’re talking with Hubspot to optimize the use of quick filters.
**For now , use only the filter ****UTM Term ****& ****create date ****(contact).**
Now that your campaign is live, the key question is: **How do you track the results?** And how can you use **accurate metrics** to measure performance and **compensate your partner fairly**?
**📊 Access the Partner Tracking Dashboard**
To make tracking simple, we’ve built a **dedicated HubSpot dashboard** where you can monitor your partner’s impact in real-time:
👉 [Partner Tracking Dashboard](https://app.hubspot.com/reports-dashboard/4419217/view/15475848)**
**
---
**🔹 ****What Can You Track?**
By using this dashboard, you can measure key performance indicators, including:
✅ **Lead & Conversion Metrics**
- 📌 **Total Leads Generated** – Number of people who filled out a form.
- 📌 **Applicants** – Leads who submitted an application.
- 📌 **Enrolled Students** – Leads who successfully converted into students.
✅ **Application & Pipeline Insights**
- 📌 **Abandoned Applications** – Leads who started an application but didn’t complete it.
- 📌 **Admissions Pipeline Overview** – Where each lead stands in the admission process.
- 📌 **Landing Page Performance** – Engagement and conversion rates of your campaign page.
---
**🔹 How to Use Filters for Better Insights?**
To refine your analysis, apply the **right dashboard filters** based on what you need to track:
🔴 **Mandatory Filters** *(Ensure accurate tracking!)*
🔍 **In-Depth Filters** *(For deeper analysis!)*
---
**🚀 Next Step: Analyze & Optimize**
Regularly check the **HubSpot Dashboard** to track your partner’s performance and optimize your campaign strategy. 📊​
---
## Questions?
Please create a github ticket here: <https://github.com/lewagon/help/issues/new/choose>
## Related
- [[Content]]

---
type: notion-import
notion-id: 24f8924af01480fbb203c40de9546e5e
source-url: https://app.notion.com/p/lewagon/AI-Chatbot-Official-documentation-24f8924af01480fbb203c40de9546e5e
imported: 2026-07-23
---
# AI Chatbot – Official documentation
# **Context**
We developed an AI-only chatbot to assist users across key touchpoints, including the application form, program pages, and other pages of the website. The chatbot is designed to autonomously guide users through these journeys, providing instant answers and streamlining the experience—without any human involvement.
The Sales & Admissions team currently spends significant time on calls answering questions that are already addressed on the website. However, the complexity of the site makes it difficult for users to quickly access key information—for instance, it can take over 10 minutes to locate the pricing of a specific bootcamp. The AI chatbot helps resolve this by offering immediate, contextual responses, reducing friction and improving user autonomy.
# **Objectives**
Deliver accurate, helpful answers to users in order to boost conversion rates on our existing conversion points (e.g. apply form clicks).
> [!note] 
> Important: this is not a new conversion channel—the AI chatbot is not intended to capture leads, but to support and enhance the user journey.
Proactively share relevant links (such as application forms or program pages) to guide users toward the next steps, while reassuring them that applying is non-binding and commitment-free.
# Specs
## Stack
- **Platform**: [chatbase.co](http://chatbase.co/)
- **Model used**: GPT-5
- **Knowledge Base**: Structured set of curated resources (see below)
- **Actions**:
    > [!note] 
    > AI actions are a set of functions or tasks that your AI agent can trigger or execute during a conversation with users. These actions enhance the conversational experience, improve efficiency, and allow the AI agent to go beyond just responding to queries. Some of these actions may include performing specific tasks, gathering information, providing insights, or even integrating with other systems.
        - Find sessions & prices
        - Search financing options
## Knowledge bases
The AI retrieves content from the following curated knowledge bases:
### **Bootcamps & Specialized Tracks**
> [!note] 
> Each of the following knowledge bases are enriched with:
- **Bootcamps**
        - Web Development Bootcamp
        - Data Science & AI Bootcamp
        - Data Engineering Bootcamp
        - Data Analytics Bootcamp
        - Growth Marketing Bootcamp
- **Skill courses**
        - Web Design & Webflow
        - Python & Machine Learning
        - Growth & Data Automation
        - Data Analytics Essentials
- **Intro course**
        - Intro to Generative AI
### **Other Knowledge Bases**
- **Default Knowledge Base** (used for generic information)
- **FAQ **→ from FAQ page of the website + resources from S&A team
        - [[Sales & Admissions Blockers Bible]]
        - [New resource about tools](https://www.notion.so/lewagon/Languages-Tools-Techniques-1888924af014801a8ba2f1d8e2932b4e?pvs=4)
        - [How to pitch AI updates](https://www.notion.so/lewagon/How-to-pitch-AI-updates-750752c272054eac8ff7fbb44e08ef6e?pvs=4)
        - [Learning Advisor 101](https://www.notion.so/lewagon/Learning-Advisor-1-0-1-b304189ea9c04861b0af36675006cb5a?pvs=4)
        - [General FAQ's for Sales & Admissions](https://www.notion.so/lewagon/FAQ-General-Technical-questions-about-our-Le-Wagon-Bootcamps-Skill-Courses-Career-Services-048db3615e034bf4a4d7ee7676857234?pvs=4)
        - [[The most frequently asked questions during calls|Mostly FAQ's during calls]]
- **Financing options table **→ [export of the financing options from Avo](https://www.lewagon.com/admin/resources/fundings)
- **Certifications **→ provided by local teams
---
# Chatbot demo
> [!embed] None
# Account
> [!note] 
> Credentials can be found in Bitwarden
[www.chatbase.co](https://www.chatbase.co/dashboard/le-wagon-bot/chatbot/DuH5W7Ee0TFFymXPX6DuT)​
# Documentation
[Introduction - ChatbaseWelcome to the Quick Start guide for Chatbase! This page will help you get up and running with Chatbase by walking you through the essential steps to set up your account, create your first AI Agent, and integrate it into your platformhttps://www.chatbase.co/docs/user-guides/quick-start/introduction](https://www.chatbase.co/docs/user-guides/quick-start/introduction)
# AI Actions
> [!note] 
> AI actions are a set of functions or tasks that your AI agent can trigger or execute during a conversation with users. These actions enhance the conversational experience, improve efficiency, and allow the AI agent to go beyond just responding to queries. Some of these actions may include performing specific tasks, gathering information, providing insights, or even integrating with other systems.
> [!note] 
> The two actions can be found in [[Automations|🦾Automations]]:
## Find sessions & prices
> This actions is used to retrieve the next sessions & prices based on user request. User will be asked to
<details><summary>**Prompt to trigger the action**</summary>
</details>
When the action is triggered [(see how)](https://app.notion.com/p/1d98924af0148024a959d436edf424b5?pvs=25#2068924af01480ac95d3ded30a317784), the chatbot automatically asks for the user’s course of interest and country. Once this information is provided, it triggers a [scenario in Make](https://eu1.make.com/372343/scenarios/3278859/edit).
![](https://app.notion.com/image/attachment%3A81ab1b90-6bc0-417c-9daa-d026e64e24b1%3ACapture_decran_2025-06-02_a_11.32.55.png?table=block&id=24f8924a-f014-8060-aa01-cf4202e53991&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
### **Session search logic**
At Le Wagon, the price of a bootcamp session depends on three key factors:
- The **course** (e.g. Web Development, Data Science),
- The **format** (full-time or part-time),
- And the **location** (on-campus or online).
To help users find relevant sessions through the chatbot, we’ve implemented a webhook-based AI action in Chatbase. This action sends a POST request to a Make.com automation, which queries a Google Sheet containing all session data.
### **Why we ask for the course and the country**
In order to avoid returning too many results and to ensure relevance, the chatbot must collect **at least the course of interest and the user’s country**. Rather than asking for a specific city (the full list of campuses is too long to present conversationally), we use the **country** input and leverage the OpenAI API to map it to a broader **campus region**.
This region-based filtering allows us to:
- Show available **on-campus sessions in nearby locations**,
- Always include **online sessions** as an option, giving users more flexibility,
- Avoid frustration for users based in regions where we don’t currently operate.
This approach ensures a smoother experience while maintaining accurate and relevant session recommendations.
## **Financing options**
> This actions is used to find the most adapted financing options based on user country.
<details><summary>**Prompt to trigger the action**</summary>
</details>
When the action is triggered [(see how)](https://app.notion.com/p/1d98924af0148024a959d436edf424b5?pvs=25#2068924af0148079a284f4b41e1abe82), the chatbot automatically asks for the user’s country. Once the information is provided, it automatically triggers a [scenario in Make](https://eu1.make.com/372343/scenarios/3302842/edit).
![](https://app.notion.com/image/attachment%3Aca6a3053-d403-4e91-8c61-4e9658a01a29%3ACapture_decran_2025-06-02_a_11.45.17.png?table=block&id=24f8924a-f014-8099-93d9-e30464f6cea0&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
This scenario searches a Google Sheets database that contains all financing options exported from Avo.
# Chatbot analysis
<details><summary>**Prompt for Chatbase analysis**</summary>
</details>
# Deployment
The chatbot was redeployed on @May 27, 2025 using [Chatbase.co](http://chatbase.co/), following technical issues with the previous platform.
> It was initially launched on @April 16, 2025 using Botpress.
### Chatbot trigger in GTM
# Updates
Updated with AI Software on @July 7, 2025
# Current issues
<!-- unhandled: transclusion_reference -->
Issue TrackingKanbanAll IssuesMy IssuesUntriaged1 more…Open1In progress0Testing0Resolved7
---
## 👀 Reviews / Feedback
[[Le Wagon Chatbot AI – Feedback Collection|Le Wagon Chatbot AI – Feedback Collection]]
## 📈 Tracking / First Results
---
> [!note] 
> **Dashboard URL: **To complete
**Other metrics:**
To complete
## 🧑‍🏫 **Learnings**
---
To complete
## Related
- [[Automations]]
- [[Bootcamps]]
- [[Content]]
- [[Data Science & AI]]
- [[Le Wagon Chatbot AI – Feedback Collection]]
- [[Sales & Admissions Blockers Bible]]
- [[Skill courses]]

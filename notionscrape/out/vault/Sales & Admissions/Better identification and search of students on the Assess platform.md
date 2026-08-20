---
type: notion-import
notion-id: 2e28924af014809cbd36c2c95e9cb7e2
source-url: https://app.notion.com/p/lewagon/Better-identification-and-search-of-students-on-the-Assess-platform-2e28924af014809cbd36c2c95e9cb7e2
imported: 2026-07-23
---
# Better identification and search of students on the Assess platform
## Release note 🚀​
A metabase dashboard is now accessible. It allows us to search for a specific students results and also computes certification metrics automatically, eliminating manual CSV exports and providing real-time insights into certification performance.
Dashboard available here : <https://metabase.lewagon.com/dashboard/479-certification>
## Summary
> [!note] 
> TODO: Explain the problem in one sentence. ***Don’t think/talk about a solution ❌***​
We currently struggle to quickly and reliably identify students on the Access platform, which creates operational friction and prevents us from properly tracking certification attempts.
## Business Impact
> [!note] 
> TODO : Explain business impact of your issue
<details><summary>**Suggested Checklist**</summary>
</details>
- ** Significant time loss for operations teams**: students frequently contact us to retrieve their information, and we must manually search session by session to find them. This happens daily during certification periods.
        -
- **Poor tracking of certification attempts: **students are entitled to two certification attempts. From the third attempt onward, the certification must be paid. At the moment, we cannot reliably identify whether a student is registering for a third attempt unless we personally know them.
        -
- **Scalability issue: **more than 1,000 students go through certification every year, making manual tracking unsustainable.
        -
- **Financial risk: **inability to correctly identify third attempts can lead to missed payments and inconsistent application of certification rules.
        -
## Context & Problem
> [!note] 
> TODO: Explain in great details the context surrounding this issue
<details><summary>**Suggested Checklist**</summary>
</details>
Access is the platform used to manage RNCP certifications. Today, student identification relies heavily on manual checks and individual knowledge of learners.
Operationally, when a student reaches out for certification-related information, teams need to search across multiple sessions to locate the correct profile. There is no efficient way to search for or identify a student globally across the platform.
Additionally, Access does not currently allow us to clearly track how many times a student has registered for a certification. As a result, we cannot systematically enforce the rule that certification attempts beyond the second one must be paid.
This creates operational inefficiencies, increases the risk of errors, and makes it difficult to ensure fair and consistent treatment of students, while also impacting revenue tracking for paid certification attempts.
## Related
- [[Assess]]
- [[Events]]

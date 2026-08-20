---
type: notion-import
notion-id: 1d18924af01480ac989dfaaa65cc9fc3
source-url: https://app.notion.com/p/lewagon/Prevent-teacher-to-be-staffed-without-active-signed-contract-1d18924af01480ac989dfaaa65cc9fc3
imported: 2026-07-23
---
# Prevent teacher to be staffed without active signed contract
## Release note 🚀​
We couldn’t implement the feature as it is, otherwise we won’t be able to staff teachers in 2025 for Q1 2026 with Kitt logic.
However, we focus the scope of the project on improving out teaching contract dashboard.
[[Required teaching contracts|🧑‍🏫Required teaching contracts]]
## Summary
> [!note] 
> TODO: Explain the problem in one sentence. ***Don’t think/talk about a solution ❌***​
Currently, teachers can be staffed and invoice us even if no signed contract is in place, as there is no automated check in Kitt to prevent this.
## Business Impact
> [!note] 
> TODO : Explain business impact of your issue
<details><summary>**Suggested Checklist**</summary>
</details>
- Risk of non-compliance with labor regulations and jeopardizing Qualiopi certification
        -
- Potential legal exposure due to teachers invoicing without a formal agreement
        -
- Time lost by Ops teams manually verifying contracts, often under tight deadlines
        -
- Increased likelihood of human error in high-volume environments (e.g., Online with 100+ teachers)
        -
- Lack of contract visibility reduces trust in internal processes and complicates batch management
        -
## Context & Problem
> [!note] 
> TODO: Explain in great details the context surrounding this issue
<details><summary>**Suggested Checklist**</summary>
</details>
Currently, checking whether a teacher has a contract is a pain point. The process is time-consuming, as we have to verify each teacher individually by going into their Kitt profile and checking the "Contract" tab.
The Crew tab isn’t reliable, it’s not up to date and doesn’t display contract information for batches using custom calendars. This makes things even more complicated for Online, where we typically manage around 20 batches and over 100 teachers at any given time.
This volume makes the process not only tedious but also prone to human error. On top of that, Online BMs often add new TAs independently and BM cannot be onboarded on how to send contract.
<details><summary>Exemple of custom calendar crew tab</summary>
</details>
<details><summary>Exemple of false information on the crew tab</summary>
</details>
## Related
- [[Batch Management]]
- [[Required teaching contracts]]

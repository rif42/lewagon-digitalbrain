---
type: notion-import
notion-id: 2a88924af01480c0a584c5d85295afbc
source-url: https://app.notion.com/p/lewagon/Create-students-group-ping-on-Slack-2a88924af01480c0a584c5d85295afbc
imported: 2026-07-23
---
# Create students group ping on Slack
## Summary
We don’t currently have a way to ping only students on the batch Slack channels, any @channel or @here also notifies teachers.
## Business Impact
This causes notification fatigue for teachers, who end up muting or ignoring batch channels. As a result, important operational updates meant for students (like reminders, deadlines, or completion rate alerts) are often missed, impacting communication efficiency and student engagement.k
## Context & Problem
Currently, all messages sent on a batch channel (e.g. #batch-2200-online) are visible to both students and teachers. However, Ops & teacher messages are often only relevant to students. Since teachers receive too many irrelevant notifications, they tend to mute or stop following those channels. This makes it difficult to communicate efficiently with students while respecting teachers’ time and focus.
A solution would be to create a dedicated Slack group (e.g. @students-batchxxx) or another system allowing Ops to ping only students when needed.
## Other Resources
[Slack documentation](https://slack.com/intl/en-gb/help/articles/212906697-Create-a-user-group) on group pings
---
## Related
- [[Automate birthday wishes in students Slack]]

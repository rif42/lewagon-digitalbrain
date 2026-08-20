---
type: notion-import
notion-id: c16d8fcde93b4a0795201839118431ed
source-url: https://app.notion.com/p/lewagon/Deposit-Amount-Variable-c16d8fcde93b4a0795201839118431ed
imported: 2026-07-23
---
# Deposit Amount Variable
## Context
We often resort to changing students’ tuition for a variety of reasons, and this can lead to some issues on the contract level. Since contracts mention the percentage and amount of the deposit students are expected to pay to confirm their seats, admission managers had to manually change these mentions in the contract every time the tuition changed.
## Solution
We’ve made a few minor changes to help with this issue.
From your camp settings, you now need to set the camp’s deposit amount 👇​
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Ff0f2fecd-c51a-4579-8905-4ed3145f4d1b%2FScreenshot_2022-11-02_at_10.28.20_AM.png?table=block&id=3021ea53-2f41-459e-8dfd-c2fa46e98ce1&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
And your contracts need to be injected with the new $CAMP_DEPOSIT variable to make sure the contract updates dynamically with every tuition change 👌​
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F3b050e37-6c51-4152-86eb-9adbaed1971d%2FScreenshot_2022-11-02_at_10.32.05_AM.png?table=block&id=37238e60-ad79-48da-b666-50e557c48a9b&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
## Related

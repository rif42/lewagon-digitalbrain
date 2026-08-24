---
type: notion-import
notion-id: 758487d1a22e4e60914e5c37d9d04198
source-url: https://app.notion.com/p/lewagon/Minijobbers-Payslips-758487d1a22e4e60914e5c37d9d04198
imported: 2026-07-23
---
# Minijobbers Payslips
> [!note] 
> This is a feature which only concerns German cities 🇩🇪​
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1074713a-a899-4626-8139-289618f559fe%2FScreenshot_2021-05-11_at_13.46.33.png?table=block&id=682a8765-77eb-4594-812a-361b6cc2d0be&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
We’ve just deployed the new MiniJobber feature to generate the monthly payslips.
You can see the [previous months closings here](https://kitt.lewagon.com/cities/berlin/mini_jobber_closings) including the month of April we did “manually” last week.
You can also have a look at the upcoming closings [here](https://kitt.lewagon.com/cities/berlin/mini_jobber_closings/upcoming) (including the coming one: May 2021).For each closing (or upcoming closing), you can view the list of payslips (or upcoming payslips), with all the details (teaching amount, extra amount, previous month delta, next month delta… etc).
You can also access a specific payslip details (days worked… etc), and if this payslip is not yet created (month not closed), you can also add an extra work assignments (i.e. a workshop, week 0, …etc). Once added, this will re-compute the payslip amounts.We will prepare a Notion document with the different steps and screens.
**Important:**
Once a month is closed, you can’t re-open it. This is definitive, and will create the payslips. SO, be super careful with this feature, and make sure you do it late in the month (to avoid closing the month, while the teacher staffing might still change for this month).
**Disclosure:**
We have a small performance issue on the upcoming closings and payslips index pages. We’re working on it, and will try to improve it asap. This is due to the fact that we have to dynamically compute all the amounts and details on the fly for each minijobber. I’ll keep you updating once this is fixed. In the meantime, be patient while the page is loading.
## Related
- [[MiniJobbers]]

---
type: notion-import
notion-id: b9f6fccfd94748e5a10f2534a8666c00
source-url: https://app.notion.com/p/lewagon/Apply-with-Source-in-URL-b9f6fccfd94748e5a10f2534a8666c00
imported: 2026-07-23
---
# Apply with Source in URL
## Context
Recently, for a partnership, we needed to easily tag applicants that came from a specific referrer (our partner in that case). This piece of information had to be visible as well in the ATS, to let the admission managers apply a specific process to these candidates (ex: discount… etc).
For Embedded Apply form, one could easily add tags that would be added to the ATS candidate page.
But sometimes, Embedded Apply form is not the best solution (especially when you want to cover lots of batches, programs and multiple territories)
## Solution
**Usage**
Now, the standard apply form in www support the source= parameter in its URL.
```
https://www.lewagon.com/(:locale/)apply?source=SOME_REFERAL_CODE​
```
When a candidate lands on the Apply form with this URL, we will automatically **store **the source value. This piece of data will be added to the apply of this candidate during the apply form flow, until the final submit.
**In Kitt’s ATS**
Once submitted, the source will be stored in the Apply sent to Kitt, and will be propagated to the ATS candidate’s page.
The information will be displayed at **Source, **in the **Application** tab, of the candidate’s page.
![](https://app.notion.com/image/https%3A%2F%2Fprod-files-secure.s3.us-west-2.amazonaws.com%2F2b6dea13-478f-4f00-aff1-afd11ed5a03f%2F464ac1bd-c7de-4ee3-b6c7-cb8b8203e971%2FUntitled.png?table=block&id=a845da05-d4fc-4b56-9e76-ad3195adae54&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=1410&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
> [!note] 
> The source will be prepended by other - when displayed in the ATS to clearly show it is a non-standard source (like friends_and_family...)
## Advanced
For those of you who have the credentials, we have also implemented a [Blazer query to filter applies by the source](https://kitt.lewagon.com/blazer/queries/2035-applies-by-source)
## Related
- [[Candidates]]

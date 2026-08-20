---
type: notion-import
notion-id: f50b53d2fe7f4ec88ed1e39dc7839cbd
source-url: https://app.notion.com/p/lewagon/Accessing-S3-logs-f50b53d2fe7f4ec88ed1e39dc7839cbd
imported: 2026-07-23
---
# Accessing S3 logs
The www website infrastructure relies on [Fastly](https://www.fastly.com/) to answer incoming HTTP traffic. 90% of the time, Fastly answers directly thanks to its caching mechanism, the 10% remaining is passed along to the Rails application, hosted on Scalingo.
SEO audit require to look at HTTP logs to analyse traffic from GoogleBot and other related user agents. We can’t rely on Scalingo router logs here, we need to ask Fastly. There is a Logging pipeline in place from Fastly to BigQuery and another one from Fastly to the wagon-www-logs S3 bucket (cf [documentation](https://docs.fastly.com/en/guides/log-streaming-amazon-s3)).
The log format used is NCSA extended/combined log format as described in the [Apache documentation](https://httpd.apache.org/docs/current/mod/mod_log_config.html#examples):
```
"%h %l %u %t\"%r\"%>s %b\"%{Referer}i\"\"%{User-agent}i\""​
```
## Downloaded logs
To connect to S3, you can use CLI or a Desktop Application like [CyberDuck](https://cyberduck.io/). Launch it and create a new bookmarked connection:
In the connection form, fill the following:
- Top dropdown: Amazon S3
- Nickname: Le Wagon - www logs
- Server: s3.eu-west-3.amazonaws.com
- Access Key ID: *secret given to you*
- Secret Access Key: *secret given to you*
- Path: /wagon-www-logs
- Download FoldeR: create a www-logs folder under your ~/Downloads one and pick it up there
Save and close the form, the new connection should appear in your bookmarks. Double click to connect to the S3 bucket.
---
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fb88f85e3-e53c-4710-a12b-2c6e7bfa4d11%2FUntitled.png?table=block&id=6e3a19ab-a7ac-4110-ab5b-a0b61f848852&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=450&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
![](https://app.notion.com/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F17f4a5be-0f24-45f5-ad14-1364309a9ae1%2FUntitled.png?table=block&id=e68dc164-6bdf-4fa3-b582-62cabdce9fc8&spaceId=2b6dea13-478f-4f00-aff1-afd11ed5a03f&width=640&userId=342d872b-594c-817d-8145-000204a2c537&cache=v2&imgBuildSrc=requestProxiedImageUrl)
Then it’s just a matter of picking the .log files you want and downloading them. Each file is 1 day of log of one of Fastly edge server, that’s why there are many files for each day.
## Concatenating log files
If you have downloaded all relevant .log files to an empty www-logs folder inside your Downloads, then you can run the following in the terminal to concatenate all these files into a single combined.log file output
```
cd~/Downloads/www-logsfind.-maxdepth1\(-name"*.log"!-name combined.log\)-print0\|sort-z|xargs-0cat>combined.logls-lthr# The last line should output the size of the new file `combined.log`​
```
## Related

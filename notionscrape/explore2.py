import email, re, json
from collections import Counter
from bs4 import BeautifulSoup
fn = 'A Guide to Pedagogical margin _ Notion.mhtml'
with open(fn, 'rb') as f:
    msg = email.message_from_binary_file(f)
html = None
for part in msg.walk():
    if part.get_content_type().startswith('text/html'):
        html = part.get_payload(decode=True)
        break
soup = BeautifulSoup(html, 'lxml')
pc = soup.select_one('.notion-page-content')
# count block types
cnt = Counter()
for tag in pc.find_all(class_=True):
    classes = tag.get('class')
    for c in classes:
        m = re.match(r'notion-(.+)-block$', c)
        if m:
            cnt[m.group(1)] += 1
print('block types:', cnt.most_common())
# sample all block types present
seen = {}
for tag in pc.find_all(class_=True):
    classes = tag.get('class')
    for c in classes:
        m = re.match(r'notion-(.+)-block$', c)
        if m:
            t = m.group(1)
            if t not in seen:
                seen[t] = tag
for t, tag in seen.items():
    print('---', t)
    print(tag.prettify()[:1000])
    print('text:', tag.get_text(strip=True)[:200])
# images
imgs = pc.find_all('img')
print('images in page', len(imgs))
for img in imgs[:3]:
    print(img.get('src'), img.get('alt'))
# links
links = pc.find_all('a', href=True)
print('links in page', len(links))
for a in links[:10]:
    print(a.get('href'), a.get_text(strip=True)[:80])

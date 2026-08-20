import email, re
from bs4 import BeautifulSoup
fn = 'A Guide to Pedagogical margin _ Notion.mhtml'
with open(fn, 'rb') as f:
    msg = email.message_from_binary_file(f)
print('Snapshot-Content-Location:', msg.get('Snapshot-Content-Location'))
html = None
for part in msg.walk():
    if part.get_content_type().startswith('text/html'):
        html = part.get_payload(decode=True)
        break
print('html len', len(html))
soup = BeautifulSoup(html, 'lxml')
print('title', soup.title.string if soup.title else None)
sb = soup.select_one('.notion-outliner-shared')
print('sidebar found', bool(sb))
if sb:
    links = sb.select('a[role="treeitem"]')
    print('treeitem links', len(links))
    for a in links[:5]:
        print('href', a.get('href'), 'text', a.get_text(strip=True)[:80])
    groups = sb.select('div[role="group"]')
    print('groups', len(groups))
pcs = soup.select('.notion-page-content')
print('page-content count', len(pcs))
for i,pc in enumerate(pcs):
    print(i, len(pc.get_text(strip=True)))
pc = max(pcs, key=lambda x: len(x.get_text(strip=True)))
for child in pc.find_all(recursive=False)[:30]:
    print(child.get('class'))

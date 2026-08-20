import email, re, sys
from bs4 import BeautifulSoup, Tag
fn = 'A Guide to Pedagogical margin _ Notion.mhtml'
sys.stdout.reconfigure(encoding='utf-8')
with open(fn, 'rb') as f:
    msg = email.message_from_binary_file(f)
html = None
for part in msg.walk():
    if part.get_content_type().startswith('text/html'):
        html = part.get_payload(decode=True)
        break
soup = BeautifulSoup(html, 'lxml')
sb = soup.select_one('.notion-outliner-shared')
# print first group structure with aria-owns
for a in sb.find_all('a', role='treeitem', limit=20):
    print('text:', a.get_text(strip=True)[:80])
    print('href:', a.get('href'))
    print('aria-owns:', a.get('aria-owns'))
    # parent group id?
    group = a.find_parent('div', role='group')
    if group:
        print('parent group id:', group.get('id'))
    print()
# print all groups
for g in sb.find_all('div', role='group', limit=5):
    print('GROUP id:', g.get('id'))
    # what treeitems are inside
    for a in g.find_all('a', role='treeitem', limit=3):
        print(' ->', a.get_text(strip=True)[:80])

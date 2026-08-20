import email, re, sys
from bs4 import BeautifulSoup
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
pc = soup.select_one('.notion-page-content')
# all links inside pc
for a in pc.find_all('a', href=True):
    href = a['href']
    if 'notion.com/p/lewagon' in href:
        print('NOTION', href, '|', a.get_text(strip=True))
    elif href.startswith('http'):
        print('EXT', href, '|', a.get_text(strip=True)[:80])
# toggle full structure
print('\n---TOGGLE FULL---')
for t in pc.find_all(class_=lambda x: x and 'notion-toggle-block' in x):
    print(t.prettify()[:4000])
    break
print('\n---CALLOUT FULL---')
for t in pc.find_all(class_=lambda x: x and 'notion-callout-block' in x):
    print(t.prettify()[:4000])
    break

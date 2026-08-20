import email, re, sys, json
from collections import Counter
from bs4 import BeautifulSoup, Tag
fn = 'A Guide to Pedagogical margin _ Notion.mhtml'
import os
# utf-8 output
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
# list all top-level children
for child in pc.find_all(recursive=False):
    classes = child.get('class') or []
    btype = None
    for c in classes:
        m = re.match(r'notion-(.+)-block$', c)
        if m:
            btype = m.group(1)
    print(btype, child.get_text(strip=True)[:120])
# find a toggle
print('\n---TOGGLE---')
for t in pc.find_all(class_=lambda x: x and 'notion-toggle-block' in x):
    print(t.prettify()[:2000])
    break
print('\n---CALLOUT---')
for t in pc.find_all(class_=lambda x: x and 'notion-callout-block' in x):
    print(t.prettify()[:2000])
    break
print('\n---IMAGE---')
for t in pc.find_all(class_=lambda x: x and 'notion-image-block' in x):
    print(t.prettify()[:2000])
    break
print('\n---CODE---')
for t in pc.find_all(class_=lambda x: x and 'notion-code-block' in x):
    print(t.prettify()[:2000])
    break

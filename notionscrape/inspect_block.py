import email, re
from bs4 import BeautifulSoup

f = r'D:\life\Work\Clients\lewagon\notionscrape\A Guide to Pedagogical margin _ Notion.mhtml'
with open(f, 'rb') as fh:
    msg = email.message_from_binary_file(fh)

html = None
for part in msg.walk():
    if part.get_content_type() == 'text/html':
        html = part.get_payload(decode=True)
        if html is None:
            html = part.get_payload(decode=False)
            if isinstance(html, str):
                html = html.encode('utf-8')
        break

if html is None:
    print('no html')
    exit(1)

soup = BeautifulSoup(html, 'lxml')
contents = soup.find_all(class_=re.compile(r'\bnotion-page-content\b'))
content = max(contents, key=lambda x: len(x.get_text()))
texts = content.find_all(class_=re.compile(r'\bnotion-text-block\b'))
for i, t in enumerate(texts[:3]):
    print('---', i, '---')
    print(t.prettify()[:4000])
    print('TEXT:', repr(t.get_text(strip=True))[:500])

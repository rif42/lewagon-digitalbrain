import email, re
from bs4 import BeautifulSoup

f = r'D:\life\Work\Clients\lewagon\notionscrape\A Guide to Pedagogical margin _ Notion.mhtml'
with open(f, 'rb') as fh:
    msg = email.message_from_binary_file(fh)
html = None
for part in msg.walk():
    if part.get_content_type().startswith('text/html'):
        html = part.get_payload(decode=True)
        break
soup = BeautifulSoup(html, 'lxml')
sb = soup.select_one('.notion-outliner-shared')
links = sb.select('a[role="treeitem"]') if sb else []
print('links', len(links))
for i, a in enumerate(links[:5]):
    print('---', i)
    # print minimal structure
    print(a.prettify()[:2500])
    print('get_text:', a.get_text(strip=True)[:100])
    # aria-labelledby target
    lab = a.get('aria-labelledby')
    if lab:
        target = soup.find(id=lab)
        print('aria-labelledby target text:', target.get_text(strip=True)[:100] if target else None)
    # first notranslate
    nt = a.find(class_=lambda x: x and 'notranslate' in x.split())
    print('notranslate text:', nt.get_text(strip=True)[:100] if nt else None)
    print('href:', a.get('href'))

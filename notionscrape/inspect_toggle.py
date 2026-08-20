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
pc = max(soup.find_all(class_=re.compile(r'\bnotion-page-content\b')), key=lambda x: len(x.get_text()))
# print toggle blocks
for tb in pc.find_all(class_=re.compile(r'\bnotion-toggle-block\b')):
    print('--- TOGGLE ---')
    print(tb.prettify()[:5000])
    print('--- END TOGGLE ---')
    break

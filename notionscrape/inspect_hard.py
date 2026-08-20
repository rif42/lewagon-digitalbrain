import email, re
from bs4 import BeautifulSoup

f = r'D:\life\Work\Clients\lewagon\notionscrape\Operations Team Wiki _ Home _ Notion.mhtml'
with open(f, 'rb') as fh:
    msg = email.message_from_binary_file(fh)
html = None
for part in msg.walk():
    if part.get_content_type().startswith('text/html'):
        html = part.get_payload(decode=True)
        break
soup = BeautifulSoup(html, 'lxml')
pc = max(soup.find_all(class_=re.compile(r'\bnotion-page-content\b')), key=lambda x: len(x.get_text()))
print('--- button ---')
for b in pc.find_all(class_=re.compile(r'\bnotion-button-block\b'))[:2]:
    print(b.prettify()[:2000])
print('--- unknown block ---')
for b in pc.find_all(class_=re.compile(r'\bnotion-unknown-block\b'))[:1]:
    print(b.prettify()[:2000])
print('--- transclusion_container ---')
for b in pc.find_all(class_=re.compile(r'\bnotion-transclusion_container-block\b'))[:1]:
    print(b.prettify()[:2000])
print('--- collection_view ---')
for b in pc.find_all(class_=re.compile(r'\bnotion-collection_view-block\b'))[:1]:
    print(b.prettify()[:4000])

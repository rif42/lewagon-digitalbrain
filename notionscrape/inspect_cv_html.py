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
cvs = pc.find_all(class_=re.compile(r'\bcollection_view(?!_page)-block\b'))
out = []
for i, cv in enumerate(cvs):
    out.append(f'--- CV {i} ---')
    out.append(cv.prettify()[:10000])
    out.append('--- END CV ---')
with open(r'D:\life\Work\Clients\lewagon\notionscrape\inspect_cv_html.txt', 'w', encoding='utf-8') as fh:
    fh.write('\n'.join(out))
print('wrote inspect_cv_html.txt')

#!/usr/bin/env python3
"""Detailed categorization of unresolved links."""
import json, re
from collections import Counter

text = open('out/vault/_report.md', encoding='utf-8').read()
section = text.split('## Unresolved Internal Links')[1].split('##')[0]
urls = re.findall(r'https://app\.notion\.com/p/[^\s`]+', section)

hierarchy = json.load(open('out/pages/_hierarchy_merged.json', encoding='utf-8'))
hierarchy_ids = {}
def walk(nodes):
    for n in nodes:
        hierarchy_ids[n['id']] = n['title']
        walk(n.get('children', []))
walk(hierarchy)

# Also load page metadata
from pathlib import Path
page_metas = {}
for jf in Path('out/pages').glob('*.json'):
    if jf.name == '_hierarchy_merged.json': continue
    data = json.load(open(jf, encoding='utf-8'))
    page_metas[data['notion_id']] = data['title']

# Categorize
name_based_pages = []  # Has a name prefix, is a real page
db_views = []           # Has ?v= parameter (database views)
pure_page_uuids = []    # Pure UUID, might be actual pages

for url in sorted(set(urls)):
    base = url.split('?')[0].split('#')[0].rstrip('/')
    seg = base.split('/')[-1]
    has_v_param = '?v=' in url or '?v=' in url.split('#')[0]
    
    if seg.startswith('lewagon/'):
        # These are all database view URLs (already skipped)
        db_views.append(url)
        continue
    
    # Extract UUID
    uid_match = re.search(r'([a-f0-9]{32})', seg.lower())
    uid = uid_match.group(1) if uid_match else None
    
    is_pure_uuid = bool(re.match(r'^[a-f0-9]{32}$', seg.lower()))
    
    if has_v_param:
        db_views.append(url)
        continue
    
    if is_pure_uuid:
        if uid in hierarchy_ids:
            name_based_pages.append((url, uid, hierarchy_ids[uid] + ' [ALREADY IN VAULT]'))
        elif uid in page_metas:
            name_based_pages.append((url, uid, page_metas[uid] + ' [HAS MHTML BUT NOT PLACED]'))
        else:
            pure_page_uuids.append((url, uid))
    else:
        # Name-based page
        name_seg = re.sub(r'-([a-f0-9]{32}).*$', '', seg)
        if uid and uid in hierarchy_ids:
            name_based_pages.append((url, uid, hierarchy_ids[uid] + ' [ALREADY IN VAULT]'))
        elif uid and uid in page_metas:
            name_based_pages.append((url, uid, page_metas[uid] + ' [HAS MHTML BUT NOT PLACED]'))
        else:
            name_based_pages.append((url, uid, name_seg))

print('=== Summary ===')
print(f'Name-based pages to download: {len([x for x in name_based_pages if "ALREADY" not in x[2] and "HAS MHTML" not in x[2]])}')
print(f'Already in vault: {len([x for x in name_based_pages if "ALREADY" in x[2]])}')
print(f'Has MHTML but unplaced: {len([x for x in name_based_pages if "HAS MHTML" in x[2]])}')
print(f'Pure UUID pages (missing): {len(pure_page_uuids)}')
print(f'Database views (skip): {len(db_views)}')

print('\n=== Name-based pages NEEDING DOWNLOAD ===')
for url, uid, name in sorted(name_based_pages, key=lambda x: x[2]):
    if 'ALREADY' not in name and 'HAS MHTML' not in name:
        print(f'  {name}')
        print(f'    URL: {url.split("?")[0]}')

print('\n=== Pure UUID pages (actual content pages, not DB views) ===')
for url, uid in sorted(pure_page_uuids):
    print(f'  {uid}')

print(f'\n--- Stats ---')
print(f'Name-based to download: {len([x for x in name_based_pages if "ALREADY" not in x[2] and "HAS MHTML" not in x[2]])}')
print(f'Already in vault: {len([x for x in name_based_pages if "ALREADY" in x[2]])}')
print(f'Has MHTML but unplaced: {len([x for x in name_based_pages if "HAS MHTML" in x[2]])}')
print(f'Pure UUID missing: {len(pure_page_uuids)}')
print(f'DB views to skip: {len(db_views)}')
total_real = len([x for x in name_based_pages if "ALREADY" not in x[2] and "HAS MHTML" not in x[2]]) + len(pure_page_uuids)
print(f'TOTAL pages to download: {total_real}')

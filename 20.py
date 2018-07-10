import json, gzip
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    print('\n'.join([json.loads(l)['text'] for l in f.readlines() if json.loads(l)['title'] == 'イギリス']))

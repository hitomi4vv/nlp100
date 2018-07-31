import json, gzip, re
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    text = '\n'.join([json.loads(l)['text'] for l in f.readlines() if json.loads(l)['title'] == 'イギリス'])
print('\n'.join(re.compile(r'(.*\[\[File:.*\]\].*)').findall(text)))

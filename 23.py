import json, gzip, re
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    text = '\n'.join([json.loads(l)['text'] for l in f.readlines() if json.loads(l)['title'] == 'イギリス'])
sections = re.compile(r'^(=+)\s*(.*?)\s*(=+)$', re.MULTILINE).findall(text)
print([s[1] for s in sections])

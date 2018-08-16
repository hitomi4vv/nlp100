import json, gzip, re
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    text = '\n'.join([json.loads(l)['text'] for l in f.readlines() if json.loads(l)['title'] == 'イギリス'])
text = re.compile(r'^\{\{基礎情報.*?$.*?^\}\}$', re.MULTILINE + re.DOTALL).findall(text)[0]
print(dict(re.compile(r'^\|(.*?)\s*=\s*(.*?)$', re.MULTILINE).findall(re.compile(r'\'{2,5}').sub('', text))))
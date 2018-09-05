import json, gzip, re, requests
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    text = '\n'.join([json.loads(l)['text'] for l in f.readlines() if json.loads(l)['title'] == 'イギリス'])
text = re.compile(r'^\{\{基礎情報.*?$.*?^\}\}$', re.MULTILINE + re.DOTALL).findall(text)[0]
pattern = r'\'{2,5}(.*?)(\1)|\[\[(?:[^:\]]+?\|)?|\]\]'
d = dict(re.compile(r'^\|(.*?)\s*=\s*(.*?)$', re.MULTILINE).findall(re.compile(pattern).sub(r'\1', text)))
print(requests.get('https://www.mediawiki.org/w/api.php', params = {
  'action': 'query',
  'titles': 'File:' + d['国旗画像'],
  'format': 'json',
  'prop': 'imageinfo',
  'iiprop': 'url'
}).json()['query']['pages'].popitem()[1]['imageinfo'][0]['url'])
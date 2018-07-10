import json, gzip
with gzip.open('jawiki-country.json.gz', 'rt') as f:
    for line in f:
        print(json.loads(line)['title'])

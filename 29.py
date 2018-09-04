import requests

print(requests.get('https://www.mediawiki.org/w/api.php', params = {
  'action': 'query',
  'titles': 'File:Flag of the United Kingdom.svg',
  'format': 'json',
  'prop': 'imageinfo',
  'iiprop': 'url'
}).json()['query']['pages'].popitem()[1]['imageinfo'][0]['url'])
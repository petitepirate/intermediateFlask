import requests

# res = requests.get('https://itunes.apple.com/search?term=jack+johnson&limit=25')
# res = requests.get('https://itunes.apple.com/search', params={'term': 'Jack Johnson', 'limit': 5})

term="Madonna"
res = requests.get('https://itunes.apple.com/search', params={'term': term, 'limit': 5})


data = res.json()

for result in data['results']:
    print(result['trackName'])
    print(result['collectionName'])

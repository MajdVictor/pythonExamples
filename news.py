import json
import requests

news = requests.get('https://api.nytimes.com/svc/mostpopular/v2/viewed/7.json?api-key=MFkYzAuJttuhkAHUTOkEDZ42rLG2sfg6')

if news.status_code == 200:
    j = json.loads(news.content)
    j= j['results']

for url in j:
    print(url['title'])
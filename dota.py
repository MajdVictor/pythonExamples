import json
import urllib3

http = urllib3.PoolManager()

heroes = http.request('GET','https://api.opendota.com/api/heroes')
heroes_dict = json.loads(heroes.data.decode('UTF-8'))

for hero in heroes_dict:
    print(hero['localized_name'])

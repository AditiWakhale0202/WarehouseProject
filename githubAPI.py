#https://api.github.com/ Parent API
#USER API: https://api.github.com/users/AditiWakhale0202
#Repo content: https://api.github.com/users/AditiWakhale0202/repos
import requests
import json
resp = requests.get('https://api.github.com/repos/django/django')
if resp.ok:
    repoItem = json.loads(resp.text or resp.content)
    print "Django repository created: " + repoItem['created_at']

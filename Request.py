import requests , json 
un = 'username' 
pw = 'password'
rapi = 'https://authserver.mojang.com/authenticate'
requestsData = json.dumps({'agent': {'name': 'Minecraft','version': 1},'username': un,'password': pw})
headers = {'Content-Type': 'application/json; charset=utf-8'}
Sess = requests.post(rapi,requestsData,headers=headers)
readJson = Sess.json()
if 'accessToken' in readJson:
  print("Valid")
else:
  print("Invalid")

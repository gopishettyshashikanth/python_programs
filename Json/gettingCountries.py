import json
with open("countries.json", "r") as f:
  data = json.load(f)
#print data  
#print data[0]['name']
for datas in data:
	print datas['name']
	print datas['code']
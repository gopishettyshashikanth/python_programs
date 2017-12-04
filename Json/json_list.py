import json
jsonData = '{"name": "Frank", "age": 39}'
jsonToPython = json.loads(jsonData)


file=open("json.txt","wb")
file.write(jsonData)
file.close()
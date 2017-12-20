import json

data = {
   'name' : 'shashi',
   'id' : 1052,
   'location' : 'Hyderabad'
}

json_str = json.dumps(data, indent=4)
print json_str
data = json.loads(json_str)

#with open('data.txt', 'w') as f:
with open('data.json', 'w') as f:

     json.dump(data, f)

with open('data.json', 'r') as f:
     data = json.load(f)     



import json

x=["provider_data","login_trans_data","service_count_data"]
#a = json.dumps(x, indent=4)
#print a

with open('test.txt', 'w') as file:

    for i in x:
        print i
    file.write(json.dumps(x)) 
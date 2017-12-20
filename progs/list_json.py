import json

x=["provider_data","login_trans_data","service_count_data"]
with open('test.txt', 'w') as file:

    for i in x:
        print i
    file.write(json.dumps(x)) 
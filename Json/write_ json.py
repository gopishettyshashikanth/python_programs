import json

# as requested in comment
exDict = {'exDict': 'exDict'}

with open('file.txt', 'w') as file:
     file.write(json.dumps(exDict))
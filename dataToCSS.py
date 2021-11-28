import json
file = open('package.json','r')
print(json.loads(file.readlines()))
file.close()
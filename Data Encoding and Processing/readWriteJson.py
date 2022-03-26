import json

#JSON String
data = {
 'name': "Jack",
 'age': 53
}

json_str = json.dumps(data)
data = json.loads(json_str)

#JSON Files
with open('file.json', 'w') as f:
    json.dump(data, f)

with open('file.json', 'r') as f:
    data = json.load(f)

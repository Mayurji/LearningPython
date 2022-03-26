import json

class JSONObject:
    def __init__(self, d):
        self.__dict__ = d

json_str = '{"name": "ACME", "shares": 50, "price": 490.1}'
dict_object = json.loads(json_str, object_hook=JSONObject)

print(f'Name: {dict_object.name}')
# Convert a JSON string like '{"name": "Ali", "age": 22}' back into a dictionary with json.loads()

import json
json_data = '{"name": "Ali", "age": 22}'
info = json.loads(json_data)
print(info)
print(type(info))
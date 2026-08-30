#  Convert a list of (name, score) tuples into JSON-compatible structures (lists/dicts) and save them.

import json
info = [("Mani",90),("Eddy",88),("Mia",67)]
new_info = []
for tup in info :
    new_info.append({"name" : tup[0], "score" : tup[1]})

print(new_info)

with open("json_8.json","w") as file :
    json.dump(new_info,file,indent=4)
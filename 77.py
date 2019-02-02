import json
with open("data.json","r") as file:
    str = file.read()
    data = json.loads(str)
    print(data)
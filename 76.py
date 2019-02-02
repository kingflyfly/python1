import json
str = """
[{"name":"yanzhe",
"gender":"maile",
"birthday":"1989-11-27"},{"name":"shanshan",
"gender":"maile",
"birthday":"1992-03-30"}]
"""
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0]["name"])
print(data[0].get("name"))
print(data[0].get("age",25))
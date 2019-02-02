import requests
"""data = {
    "name":"yanzhe",
    "age":29,
    "sex":"nan"
}
"""
r  = requests.get("http://httpbin.org/get")
print(type(r.text))
print(r.json())
print(type(r.json()))
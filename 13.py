import requests
data = {"name":"yanzhe","age":"18"}
r = requests.post("http://httpbin.org/post",data=data)
print(r.text)
import requests
r = requests.get("http://www.taobao.com",timeout=0.0001)
print(r.status_code)
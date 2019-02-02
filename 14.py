import requests
r  = requests.get("http://www.jianshu.com")
print(r.status_code)
print(r.headers)
print(r.url)
print(r.cookies)
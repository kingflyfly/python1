import requests
t = requests.get("https://www.baidu.com/favicon.ico")
with open("favicon.ico","wb") as e:
    e.write(t.content)
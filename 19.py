import requests
reponse = requests.get("http://www.12306.cn")
print(reponse.status_code)
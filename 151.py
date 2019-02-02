import requests
proxy = "182.61.170.45:3128"
proxies = {
    "http":"http://" + proxy,
    "https":"https://" + proxy
}
try:
    reponse = requests.get("http://httpbin.org/get",proxies = proxies)
    print(reponse.text)
except requests.exceptions.ConnectionError as e:
    print(e.args)
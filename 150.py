from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener
proxy = "58.55.201.117:9999"
proxy_handler = ProxyHandler({
    "http":"http://" + proxy,
    "https":"https://" + proxy
})
opener = build_opener(proxy_handler)
try:
    reponse = opener.open("http://httpbin.org/get")
    print(reponse.read().decode("utf-8"))
except URLError as e:
    print(e.reason)
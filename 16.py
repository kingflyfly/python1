import requests
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
r = requests.get("http://www.zhihu.com")
print(type(r))
print(r.cookies)
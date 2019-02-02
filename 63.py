from pyquery import PyQuery as pq
import requests
doc = pq(url="http://www.taobao.com")
print(doc("title"))
print(doc("title").text())
print("\n")
html = pq(requests.get("http://www.jd.com").text)
print(html("title"))
print(html("title").text())
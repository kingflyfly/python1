from urllib import request,parse
url = "http://httpbin.org/post"
headers = {"User-agent":' Mozilla/4.0 (compatible; MSIE S. S; Windows NT )',
          "Host":"httpbin.org"
           }
dict = {"name":"Germey"}
data = bytes(parse.urlencode(dict),encoding="utf-8")
req = request.Request(url=url,data=data,headers=headers,method="POST")
reponse = request.urlopen(req)
print(reponse.read().decode("utf-8"))

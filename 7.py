from urllib import error,request
try:
    response = request.urlopen("http://www.baidu.com")
except error.HTTPError as e:
    print(e.reason)
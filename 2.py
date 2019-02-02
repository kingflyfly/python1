from urllib import request
from urllib import parse
data = bytes(parse.urlencode({"world":"hello"}),encoding="utf-8")
request = request.urlopen("http://httpbin.org/post",data =data)
print(request.read().decode("utf-8"))

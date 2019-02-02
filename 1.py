from urllib import request
t = request.urlopen("https://www.baidu.com")
p = t.read().decode("utf-8")
print(type(t))
print(t.status)
print(t.getheaders())
print(t.getheader("Server"))
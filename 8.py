from urllib import parse
result = parse.urlparse("http://www.baidu.com/index.html;user?id=S#comment")
print(type(result),result)
from urllib import request
import socket
from urllib import error
try:
    reponse = request.urlopen("http://httpbin.org/get",timeout=0.1)
    print(reponse.read().decode("utf-8"))
except error.URLError as e:
    if isinstance(e.reason,socket.timeout):
        print("time out")
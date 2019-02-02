import requests
import re
header = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
}
r = requests.get("https://www.zhihu.com/explore",headers=header)
pattern = re.compile("explore-feed.*?question_link.*?>(.*?)</a>",re.S)
t = re.findall(pattern,r.text)
print(pattern)
print(t)
for
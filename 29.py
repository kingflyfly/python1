import re
import requests
import json
for i in range(0,91,10):
    url = "https://maoyan.com/board/4?offset={0}".format(i)
    content = requests.get(url)
    r = content.text
    results = re.findall('<dd>.*?board-index.*?>(\d+)</i>.*?'
                    + 'data-src="(.*?)".*?name"><a.*?>(.*?)'
                    + '</a>.*?star">(.*?)</p>.*?releasetime">'
                    + '(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',r,re.S)
    for item in results:
        p = {}
        p["index"]=item[0]
        p["image"]=item[1]
        p["title"]=item[2].strip()
        p["actor"]=item[3].strip()[3:]
        p["time"]=item[4].strip()[5:]
        p["socre"]=item[5].strip()+item[6].strip()
        with open("result.txt","a",encoding="utf-8") as f:
            f.write(json.dumps(p,ensure_ascii=False)+'\n')
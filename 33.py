import re
import requests
import json
import time
from requests.exceptions import RequestException
def get_one_page(url):
    try:
        content = requests.get(url)
        if content.status_code == 200:
            return content.text
        return None
    except RequestException:
        return None
def parse_on_page(url):
    results = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?'
                    + 'data-src="(.*?)".*?name"><a.*?>(.*?)'
                    + '</a>.*?star">(.*?)</p>.*?releasetime">'
                    + '(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',re.S)
    items = re.findall(results,url)
    for item in items:
        yield {
        "index":item[0],
        "image":item[1],
        "title":item[2].strip(),
        "actor":item[3].strip()[3:],
        "time":item[4].strip()[5:],
        "socre":item[5].strip()+item[6].strip(),
        }
def write_to_file(content):
    with open("result.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
def main(offset):
    url = "https://maoyan.com/board/4?offset={0}".format(str(offset))
    html = get_one_page(url)
    for item in parse_on_page(html):
        print(item)
        write_to_file(item)
if __name__ == "__main__":
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)
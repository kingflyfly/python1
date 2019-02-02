from urllib.parse import urlencode
import requests
import os
from hashlib import md5
def get_page(offset):
    headers = {
        'Host': 'www.toutiao.com',
        'Referer': 'https://www.toutiao.com/search/?keyword=%E8%A1%97%E6%8B%8D',
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        'X-Requested-With': 'XMLHttpRequest',
    }
    params = {"aid": 24,
              "offset": offset,
              "format": "json",
              "keyword": "街拍",
              "autoload": "true",
              "count": 20,
              "cur_tab": 1,
              "from": "search_tab",
              "pd": "synthesis"
              }
    base_url = "https://www.toutiao.com/api/search/content/?"
    url = base_url + urlencode(params)
    try:
        t  = requests.get(url,headers=headers)
        if t.status_code == 200:
            return t.json()
    except requests.ConnectionError as e:
        print('Error', e.args)
def get_image(json):
    if json.get("data"):
        for item in json.get("data"):
            title = item.get("title")
            images = item.get("image_list")
            if images:
                for image in images:
                    yield {
                    "image":image.get("url"),
                    "title":title
                    }
def save_image(item):
    if not os.path.exists(item.get("title")):
        os.mkdir(item.get("title"))
    try:
        reponse = requests.get(item.get("image"))
        if reponse.status_code == 200:
            file_path = "{0}/{1}.{2}".format(item.get("title"), md5(reponse.content).hexdigest(), "jpg")
            if not os.path.exists(file_path):
                with open("file_path", "wb") as f:
                    f.write(reponse.content)
    except requests.ConnectionError:
        print("fail")
for offset in range(0,200,20):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)

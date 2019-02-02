from urllib.parse import urlencode
from pyquery import PyQuery as pq
import requests
base_url = 'https://m.weibo.cn/api/container/getIndex?'
headers = {
    'Host': 'm.weibo.cn',
    'Referer': 'https://m.weibo.cn/u/2830678474',
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    'X-Requested-With': 'XMLHttpRequest',
}
params = {
    'type': 'uid',
    'value': '2830678474',
    'containerid': '1076032830678474',
    "since_id":"4324504760793878"
}
url = base_url + urlencode(params)
print(url)
def get_page(page):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            print(response.json())
            return response.json()
    except requests.ConnectionError as e:
        print('Error', e.args)

def parse_page(json):
    if json:
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            if item:
                weibo = {}
                weibo['id'] = item.get("id")
                weibo['text'] = pq(item.get('text')).text()
                weibo['attitudes'] = item.get('attitudes_count')
                weibo['comments'] = item.get('comments_count')
                weibo['reposts'] = item.get('reposts_count')
                print(weibo)
            else:
                print(1)
json = get_page(url)
parse_page(json)

with open("./result.txt","r") as f:
    t = f.read()
    for item in t:
        print(item)
        item1 = item.get('mblog')
        weibo = {}
        weibo['id'] = item1.get("id")
        weibo['text'] = pq(item1.get('text')).text()
        weibo['attitudes'] = item1.get('attitudes_count')
        weibo['comments'] = item1.get('comments_count')
        weibo['reposts'] = item1.get('reposts_count')
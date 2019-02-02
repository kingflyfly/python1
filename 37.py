from lxml import etree
html = etree.parse("./test.html",etree.HTMLParser())
results  = html.xpath('//li[@class="item-0"]/a/text()')
print(results)
for result in results:
    print(result)
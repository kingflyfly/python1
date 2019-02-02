from lxml import etree
html = etree.parse("./test.html",etree.HTMLParser())
print(html)
result = html.xpath('//li/a/@href')
print(result)
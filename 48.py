from lxml import etree
html = etree.parse("./test2.html",etree.HTMLParser())
result = html.xpath('//p[@class="releasetime"]/text()')
print(result)

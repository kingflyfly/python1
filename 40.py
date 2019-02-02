from lxml import etree
text = """<li class="item item-0"><a href="link1.html">first item</a></li>"""
html = etree.HTML(text)
result = html.xpath('//li[contains(@class,"item")]/a/text()')
print(result)
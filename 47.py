from lxml import etree
html = etree.parse("./test2.html",etree.HTMLParser())
#print(html)
result = html.xpath('//a[@href="/films/2641"]/../@class')
result1 = html.xpath('//div[@class="movie-item-info"]/../@class')
result2 = html.xpath('//p[@class="name"]/../@class')
result3 = html.xpath('//img[@src="//s0.meituan.net/bs/?f=myfe/mywww:/image/loading_2.e3d934bf.png"]/../@data-val')
print(result)
print(result1)
print(result2)
print(result3)
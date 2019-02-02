from pyquery import PyQuery as pq
html = """<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-O">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item 1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="links.html"＞ fifth item</a></li>
</ul>
</div>
</div>"""
doc = pq(html)
a = doc(".item-0.active a")
print(a,type(a))
print(a.attr.href)
doc1 =pq(html)
a1 = doc("a")
print(a1)
print(a1.attr("href"))
print(a1.attr.href)
for item in a1.items():
    print(item.attr("href"))
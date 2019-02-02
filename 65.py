from pyquery import PyQuery as pq
html = """<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-l"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class ="bold">third item</span></a></li>
<li class="item-1 active"><a href＝"link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>"""
doc = pq(html)
items = doc(".list")
print(items)
lis = items.find("li")
print(lis)
print(type(lis))
lis2 = items.children()
print(type(lis2))
print(lis2)
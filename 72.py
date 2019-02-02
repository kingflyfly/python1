from pyquery import PyQuery as pq
html ="""
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
"""
doc = pq(html)
li = doc(".item-0.active")
print(li)
li.attr("name","link")
print(li)
li.text("change-item")
print(li)
print(li.html("<span>df</span>"))
from pyquery import PyQuery as pq
html = """<div class="wrap">
Hello,World
<p> This is a paragraph.</p>
</div>"""
doc = pq(html)
warp = doc(".wrap")
print(warp.text())
warp.find('p').remove()
print(warp.text())
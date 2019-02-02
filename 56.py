from bs4 import BeautifulSoup
html = """<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class ="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="elernent">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div >
</div>"""

soup = BeautifulSoup(html,"lxml")
print(soup.find_all(name="ul"))
print(soup.find_all(name="ul")[0])
for ul in soup.find_all(name="ul"):
    print(ul.find_all(name="li"))
    for li in ul.find_all(name="li"):
        print(li.string)
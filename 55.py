from bs4 import BeautifulSoup
html="""<html>
<body>
<p class="story">
Once upon a time there were three little sisters; and t heir names were
<a href="http://example.com/elsie" class ="sister" id="link1">Bob</a><a href="http://example.com/lacie"
class="sister" id="link2">Lacie</a>
</p>"""

soup = BeautifulSoup(html,"lxml")
print(soup.a)
print(type(soup.a))
print(soup.a.string)
print(soup.a.next_sibling)
print(soup.a.next_sibling.text)
print(soup.a.next_sibling.string)
print(soup.a.parents)
print(type(soup.a.parents))
print(list(soup.a.parents))
print(list(soup.a.parents)[0].attrs["class"])
print(list(soup.a.parents)[0]["class"])
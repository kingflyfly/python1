from bs4 import BeautifulSoup
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
    Once upon a time there were three little sisters ; and t heir names were
    <a href="http://example.com/elsie" class="sister" id= "linkl">
<span>Elsie</span>
</a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
and
<a href ="http://example.com/title" class="sister" id="link3">Tillie</a>
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,"lxml")
print(soup.p.contents)
print(soup.a.parent)

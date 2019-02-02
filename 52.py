from bs4 import BeautifulSoup
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
"""
soup = BeautifulSoup(html,"lxml")
#print(soup.prettify())
print(soup.head)
print(soup.head.string)
print(soup.head.title)
print(soup.head.title.string)
print(soup.head.title.name)
print(soup.title)
print(soup.title.string)
print(soup.title.name)
print(type(soup.head.title))
print(soup.head.name)
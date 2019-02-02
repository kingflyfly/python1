from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>hello</p>","lxml")
print(soup.p.string)
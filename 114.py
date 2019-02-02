import time
from selenium import webdriver
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
browser.get("https://www.jd.com")
browser.get("https://www.taobao.com")
browser.back()
time.sleep(1)
browser.forward()
browser.close()
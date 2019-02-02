from selenium import webdriver
from selenium.common.exceptions import TimeoutException,NoSuchElementException
browser = webdriver.Chrome()
browser.get("https://www.baidu.com")
try:
    browser.find_element_by_id("hello")
except NoSuchElementException:
    print("hahah")
finally:
    browser.close()
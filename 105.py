from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.taobao.com")
input = browser.find_element_by_id("q")
input.send_keys("iphone")
time.sleep(2)
input.clear()
input.send_keys("ipad")
button= browser.find_element_by_class_name ("btn-search")
button.click()
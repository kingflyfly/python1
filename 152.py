from selenium import webdriver
proxy = "112.87.70.112:9999"
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--proxy-server=http://" + proxy)
browser = webdriver.Chrome(chrome_options = chrome_options)
browser.get("http://httpbin.org/get")
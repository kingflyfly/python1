from selenium import webdriver
from selenium.webdriver import ActionChains
browser = webdriver.Chrome()
url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
browser.get(url)
browser.switch_to_frame("ifameResult")
source = browser.find_element_by_css_selector("#draggable")
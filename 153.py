from selenium  import webdriver
service_args = [
    "--proxy=112.87.70.112:9999",
    "--proxy-type=http"
]
browser = webdriver.Chrome(service_args=service_args)
browser.get("http://httpbin.org/get")
print(browser.page_source)
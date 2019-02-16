from selenium import webdriver



driver = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title
#driver.close()

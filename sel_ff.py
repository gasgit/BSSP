from selenium import webdriver


driver = webdriver.Firefox()
driver.get('https://www.google.ie/')

inputElement = driver.find_element_by_name("q")
inputElement.send_keys('cootehill, cavan')
inputElement.submit() 

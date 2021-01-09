import time
from selenium import webdriver

link = "http://suninjuly.github.io/find_xpath_form"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    input_first_name = browser.find_element_by_xpath("//input[@name='first_name']")
    input_first_name.send_keys("First_name")
    input_last_name = browser.find_element_by_xpath("//input[@name='last_name']")
    input_last_name.send_keys("Last_name")
    input_city = browser.find_element_by_xpath("//input[@class='form-control city']")
    input_city.send_keys("City")
    input_country = browser.find_element_by_xpath("//input[@id='country']")
    input_country.send_keys("Country")
    button = browser.find_element_by_xpath("//button[@type='submit']")
    button.click()
finally:
    time.sleep(30)
    browser.quit()

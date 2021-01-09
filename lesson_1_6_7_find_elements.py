import time
from selenium import webdriver

link = "http://suninjuly.github.io/huge_form.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements_by_tag_name("input")
    for element in elements:
        element.send_keys("txt")
    button = browser.find_element_by_class_name("btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()

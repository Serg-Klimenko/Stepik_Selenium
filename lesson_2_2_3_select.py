from selenium import webdriver
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    s = int(num1) + int(num2)
    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(f"[value='{s}'").click()
    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(30)
    browser.quit()

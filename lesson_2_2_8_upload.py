from selenium import webdriver
import os
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("[name='firstname']").send_keys("First")
    browser.find_element_by_css_selector("[name='lastname']").send_keys("Last")
    browser.find_element_by_css_selector(("[name='email']")).send_keys("email@email.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "file.txt")
    browser.find_element_by_id("file").send_keys(file_path)
    browser.find_element_by_css_selector("button.btn").click()
finally:
    time.sleep(30)
    browser.quit()

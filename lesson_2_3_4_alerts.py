from selenium import webdriver
import time
import math


def calc(x):
    """
    calculate value ______________
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_css_selector("button.btn").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    browser.find_element_by_id("answer").send_keys(str(y))
    browser.find_element_by_css_selector("button.btn").click()

finally:
    time.sleep(30)
    browser.quit()
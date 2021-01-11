from selenium import webdriver
import time
import math


def calc(x):
    """
    calculate value ______________
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    # open page
    browser.get(link)
    # find picture with treasurebox
    treasure = browser.find_element_by_id("treasure")
    # get value of attribute valuex
    x = treasure.get_attribute("valuex")
    # calculate mathematical function calc
    y = calc(x)
    # enter function's result in text field
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(str(y))
    # select checkbox I'm robot
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    # select radiobutton Robots rule!
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    # click button Submit
    submit = browser.find_element_by_css_selector("button.btn")
    submit.click()


finally:
    time.sleep(30)
    browser.quit()

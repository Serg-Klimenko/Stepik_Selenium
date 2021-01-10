from selenium import webdriver
import time
import math


def calc(x):
    """
    calculate value ______________
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    # read value of element X on the page
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    # calculate mathematical function
    y = calc(x)
    # enter result of function in input field
    input_field = browser.find_element_by_id("answer")
    input_field.send_keys(str(y))
    # select  checkbox I'm the robot
    checkbox = browser.find_element_by_id("robotCheckbox")
    checkbox.click()
    # select radiobutton Robots rule!
    radiobutton = browser.find_element_by_id("robotsRule")
    radiobutton.click()
    # press button Submit
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    time.sleep(30)
    browser.quit()

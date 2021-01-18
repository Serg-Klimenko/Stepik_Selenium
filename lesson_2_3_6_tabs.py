from selenium import webdriver
import time
import math


def calc(x):
    """
    calculate value ______________
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    # open page
    browser.get(link)
    # click to button
    browser.find_element_by_css_selector("button.trollface").click()
    # move to new opened tab
    new_tab = browser.window_handles[1]
    browser.switch_to.window(new_tab)
    # find value for calculation
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    # enter result of calculation to text field
    browser.find_element_by_id("answer").send_keys(str(y))
    # click the button
    browser.find_element_by_css_selector("button.btn").click()
finally:
    # close browser
    time.sleep(30)
    browser.quit()

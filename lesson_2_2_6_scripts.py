from selenium import webdriver
import time
import math


def calc(x):
    """
    calculate value ______________
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("input_value").text
    y = calc(int(x))
    browser.find_element_by_id("answer").send_keys(str(y))
    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element_by_id("robotCheckbox").click()
    browser.find_element_by_id("robotsRule").click()
    button.click()
finally:
    time.sleep(30)
    browser.quit()

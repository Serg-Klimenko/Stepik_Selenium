from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math


def calc(x):
    """
    calculate value ______________
    """
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    # open page
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # find button "Book"
    button = browser.find_element_by_id("book")
    # wait for price equal $100
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    # press button "Book"
    button.click()
    # find value for calculation
    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    # enter result of calculation to text field
    browser.find_element_by_id("answer").send_keys(str(y))
    # click the button
    browser.find_element_by_id("solve").click()
finally:
    time.sleep(30)
    # close browser
    browser.quit()

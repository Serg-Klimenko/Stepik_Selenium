import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    # disable ChromeDevTools's logging on display
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    browser = webdriver.Chrome(options=options)
    yield browser
    # this part will be execute after test was finished
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize("url", ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, url):
    link = f"https://stepik.org/lesson/{url}/step/1"
    browser.get(link)
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    # send result of calculation to textarea
    browser.find_element_by_class_name("textarea").send_keys(str(math.log(int(time.time()))))
    # press button submit
    browser.find_element_by_class_name("submit-submission").click()
    WebDriverWait(browser, 5).until(
        EC.presence_of_element_located((By.TAG_NAME, "pre"))
    )
    res = browser.find_element_by_class_name("smart-hints__hint").text
    assert res == "Correct!"

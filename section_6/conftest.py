import pytest
from selenium import webdriver

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

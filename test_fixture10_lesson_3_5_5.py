import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    # this part will be execute after test was finished
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():
    # call fixture in the test (send it as atribute)
    def test_guest_should_see_login_link(self, browser):
        print("start test 1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test 1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test 2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test 2")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")

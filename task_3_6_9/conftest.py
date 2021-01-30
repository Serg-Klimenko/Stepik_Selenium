#############################################################################
#
# Я уже понял, что нужно было сделать новый репозиторий. Не знал, что нельзя
# просто скопировать файл или папку без клонирования всего проекта. Мне такие 
# случаи тоже попались на проверке.Предлагаю понять и простить). 
#
###############################################################################
import pytest
from selenium import webdriver



def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="es",
                     help="Choose language: es or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        # disable ChromeDevTools's logging on display
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    # this part will be execute after test was finished
    print("\nquit browser..")
    browser.quit()

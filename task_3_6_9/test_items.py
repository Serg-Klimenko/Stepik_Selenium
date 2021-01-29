# launch test in chrome: pytest --language=es test_items.py
# launch test in firefox: pytest --language=es --browser_name=firefox test_items.py
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_guest_should_see_button_basket_on_spanish_language(browser):
    browser.get(link)
    time.sleep(30)
    # test for spanish language only
    button_text = browser.find_element_by_css_selector("button.btn-add-to-basket").text
    assert button_text == "Añadir al carrito"

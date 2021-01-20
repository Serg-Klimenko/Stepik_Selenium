import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestUniqueSelectors(unittest.TestCase):
    def test_registration1(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link1)
        # Заполняем обязательные поля
        browser.find_element_by_css_selector("div.first_block input.first").send_keys("First_name")
        browser.find_element_by_css_selector("div.first_block input.second").send_keys("Last_name")
        browser.find_element_by_class_name("third").send_keys("email@email.com")
        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()
        # Ожидаем загрузку страницы
        WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         f"Expected string 'Congratulations! You have successfully registered!', "
                         f"actual string - '{welcome_text}'"
                         )

    def test_registration2(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link2)
        # Заполняем обязательные поля
        browser.find_element_by_css_selector("div.first_block input.first").send_keys("First_name")
        browser.find_element_by_css_selector("div.first_block input.second").send_keys("Last_name")
        browser.find_element_by_class_name("third").send_keys("email@email.com")
        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()
        # Ожидаем загрузку страницы
        WebDriverWait(browser, 2).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!",
                         f"Expected string 'Congratulations! You have successfully registered!', "
                         f"actual string - '{welcome_text}'"
                         )


if __name__ == "__main__":
    unittest.main()

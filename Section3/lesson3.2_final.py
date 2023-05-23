
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()

class TestAssert(unittest.TestCase):
    def test_1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
        selectors = [".first_block .first", ".first_block .second", ".first_block .third"]
        for selector in selectors:
            element = browser.find_element(By.CSS_SELECTOR, selector)
            element.send_keys("test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        
        # находим элемент, содержащий текст
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        welcome_text_expected = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, welcome_text_expected, "Welcome text should be the same!")
        
    def test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)
        selectors = [".first_block .first", ".first_block .second", ".first_block .third"]
        for selector in selectors:
            element = browser.find_element(By.CSS_SELECTOR, selector)
            element.send_keys("test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
        
        # находим элемент, содержащий текст
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        welcome_text_expected = "Congratulations! You have successfully registered!"
        self.assertEqual(welcome_text, welcome_text_expected, "Welcome text should be the same!")
        
if __name__ == "__main__":
        unittest.main()
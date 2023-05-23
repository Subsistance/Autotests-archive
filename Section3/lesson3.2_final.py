
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAssert(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def fillForm(self, link):
        browser = self.browser
        browser.implicitly_wait(5)
        browser.get(link)
        
        selectors = [".first_block .first", ".first_block .second", ".first_block .third"]
        for selector in selectors:
            element = browser.find_element(By.CSS_SELECTOR, selector)
            element.send_keys("test")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        
        # находим элемент, содержащий текст
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        return welcome_text
        
    def testRegistration1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        registration_result = self.fillForm(link)
        
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)
        
    def testRegistration2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        registration_result = self.fillForm(link)
        
        self.assertEqual("Congratulations! You have successfully registered!", registration_result)
        
if __name__ == "__main__":
        unittest.main()
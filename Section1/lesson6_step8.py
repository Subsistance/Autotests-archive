from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_xpath_form"
list = ['test', 'bla', 'bla bla', 'brrrr']

try:
    browser.get(link)
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys(random.choice(list))

    button = browser.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
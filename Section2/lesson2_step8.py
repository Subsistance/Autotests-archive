from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

  
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"

try:
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, '[name="firstname"]').send_keys('test1')
    input2 = browser.find_element(By.CSS_SELECTOR, '[name="lastname"]').send_keys('test2')
    input3 = browser.find_element(By.CSS_SELECTOR, '[name="email"]').send_keys('test3@mail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "file_example.txt"
    file_path = os.path.join(current_dir, file_name)
    element = browser.find_element(By.CSS_SELECTOR, "#file")
    element.send_keys(file_path)
    time.sleep(1)
    
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
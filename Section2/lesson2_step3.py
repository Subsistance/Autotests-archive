from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math

  
link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try: 
    browser.get(link)
    num1 = int(browser.find_element(By.ID, 'num1').text)
    num2 = int(browser.find_element(By.ID, 'num2').text)
    
    sum = num1 + num2

    select = Select(browser.find_element(By.CSS_SELECTOR, '.custom-select'))
    select.select_by_value(str(sum))

    time.sleep(3)
    
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "https://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try: 
    browser.get(link)
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '.form-control').send_keys(y)
    input2 = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]').click()
    input3 = browser.find_element(By.CSS_SELECTOR, '[type="radio"]#robotsRule').click()

    time.sleep(3)
    
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
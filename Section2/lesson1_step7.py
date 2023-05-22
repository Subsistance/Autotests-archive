from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()

try: 
    browser.get(link)
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
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
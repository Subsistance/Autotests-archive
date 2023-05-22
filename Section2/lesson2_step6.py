from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"

try:
    browser.get(link)
    x = int(browser.find_element(By.ID, "input_value").text)
    equals = calc(x)
    
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control").send_keys(equals)
    input2 = browser.find_element(By.CSS_SELECTOR, '[type="checkbox"]')
    input3 = browser.find_element(By.ID, 'robotsRule')

    
    button = browser.find_element(By.CSS_SELECTOR, ".btn")
    browser.execute_script('return arguments[0].scrollIntoView(true);', button)
    input2.click()
    input3.click()
    time.sleep(1)
    button.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
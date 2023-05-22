from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser.get(link)
    button_first = browser.find_element(By.CSS_SELECTOR, ".btn-primary").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x = int(browser.find_element(By.ID, "input_value").text)
    equals = calc(x)
    
    input = browser.find_element(By.ID, 'answer').send_keys(equals)

    button_second = browser.find_element(By.CSS_SELECTOR, ".btn")
    time.sleep(1)
    button_second.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
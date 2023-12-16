from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calculation(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

try:
    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    button.click()
    
    x = int(browser.find_element(By.ID, "input_value").text)
    result = calculation(x)
    input = browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(result)
    buttonSubmit = browser.find_element(By.CSS_SELECTOR, "#solve").click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
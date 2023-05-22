from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/find_link_text"

try:
# подготовка для теста
# открываем страницу первого товара
# данный сайт не существует, этот код приведен только для примера
	browser.get("https://www.ozon.ru/product/generator-benzinovyy-partner-for-garden-4000-3-5-kvt-7-l-s-178870328/")
	sleep(3)

# добавляем товар в корзину
	add_button = browser.find_element(By.CSS_SELECTOR, ".pl9.x5-a.x5-f1")
	add_button.click()


# тестовый сценарий
# открываем корзину
	browser.find_element(By.CSS_SELECTOR, "div.dn5 > a:nth-child(4)").click()

# ищем все добавленные товары
	goods = browser.find_elements(By.CSS_SELECTOR, "div.bg")
	sleep(3)
# проверяем, что количество товаров равно 1
	assert len(goods) == 1

finally:
	browser.quit()

# не забываем оставить пустую строку в конце файла
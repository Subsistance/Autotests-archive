from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_add_to_basket_btn(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    # optional wait to see the language on page if needed
    # time.sleep(3)
    
    # Find the 'Add to Basket' button
    add_to_basket_btn = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    # Assert that the 'Add to Basket' button is present
    assert add_to_basket_btn is not None, "The 'Add to Basket' button is not present on the page"
import pytest
import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from configparser import ConfigParser

@pytest.fixture(scope='module')
def urls_array():
    print("\nGetting urls from config")
    config = ConfigParser()
    config.read('config.ini')

    urls = {
        'url1': config.get('urls', 'url1'),
        'url2': config.get('urls', 'url2'),
        'url3': config.get('urls', 'url3'),
        'url4': config.get('urls', 'url4'),
        'url5': config.get('urls', 'url5'),
        'url6': config.get('urls', 'url6'),
        'url7': config.get('urls', 'url7'),
        'url8': config.get('urls', 'url8'),
    }
    return urls

@pytest.fixture(scope="function")
def browser():

    print("\nStart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nQuit browser..")
    browser.quit()

def login(browser):
    config = ConfigParser()
    config.read('config.ini')

    username = config.get('credentials', 'username')
    password = config.get('credentials', 'password')
    
    link = "https://stepik.org/lesson/236895/step/1?auth=login"
    browser.implicitly_wait(5)
    browser.get(link)
    
    username_field = browser.find_element(By.CSS_SELECTOR, "#id_login_email")
    password_field = browser.find_element(By.CSS_SELECTOR, "#id_login_password")
    
    username_field.send_keys(username)
    password_field.send_keys(password)
    
    button = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-form__btn"))
    )
    button.click()
    
    try:
        WebDriverWait(browser, 3).until_not(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".light-tabs"))
        )
        print("Login successful, no login popup present.")
    except TimeoutException:
        print("Login popup still present.")
    
@pytest.mark.parametrize('url_key', ["url1", "url2", "url3", "url4", "url5", "url6", "url7", "url8"])
def test_time_and_urls(browser, urls_array, url_key):
    login(browser)
    
    answer = math.log(int(time.time()))
    
    url_part = urls_array[url_key]
    link = f"https://stepik.org/lesson/{url_part}/step/1/"
    browser.get(link)
    
    time.sleep(5)
    text_area = browser.find_element(By.CSS_SELECTOR, ".ember-text-area")
    text_area.clear()
    text_area.send_keys(str(answer))
    
    button = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
    )
    button.click()
    
    # Wait for and assert the presence of "Correct!" text on the page
    try:
        WebDriverWait(browser, 3).until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Correct!')]"))
        )
    except TimeoutException:
        assert False, "'Correct!' text is not present on the page"
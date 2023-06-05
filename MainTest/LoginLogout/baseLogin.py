import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import sys
sys.path.append('../ElementLocator')
sys.path.append('../DataStorage')
from ElementLocator.locator import elem
from DataStorage.data import inputan

def test_success_login(driver): #test cases 2
    driver.get(inputan.baseUrl)
    driver.implicitly_wait(10)
    driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
    driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
    driver.find_element(By.CLASS_NAME, elem.loginButton).click()
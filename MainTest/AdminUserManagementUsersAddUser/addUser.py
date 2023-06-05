import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import sys
sys.path.append('../ElementLocator')
sys.path.append('../DataStorage')

from ElementLocator.locator import elem
from DataStorage.data import inputan

class TestUsers(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_add_user_page(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()

        driver.find_element(By.CSS_SELECTOR, elem.adminButton).click()
        driver.find_element(By.CSS_SELECTOR, elem.addUserButton).click()
        add_user_label = driver.find_element(By.CSS_SELECTOR, elem.addUserTitle)

        self.assertTrue(add_user_label.is_displayed())

if __name__ == '__main__':
    unittest.main()
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

class TestDeleteUsers(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_delete_user_page(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()

        driver.find_element(By.CSS_SELECTOR, elem.adminButton).click()
        driver.find_element(By.CSS_SELECTOR, elem.usersCellDeleteButton).click()
        delete_user_confirmation_title = driver.find_element(By.CSS_SELECTOR, elem.userDeleteConfirmationTitle)

        self.assertTrue(delete_user_confirmation_title.is_displayed())

    def test_delete_user(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()

        driver.find_element(By.CSS_SELECTOR, elem.adminButton).click()
        driver.find_element(By.CSS_SELECTOR, elem.usersCellDeleteButton).click()
        driver.find_element(By.CSS_SELECTOR, elem.userDeleteConfirmationYesButton).click()
        user_delete_toast = driver.find_element(By.CSS_SELECTOR, elem.userDeleteToast).text
        add_user_button = driver.find_element(By.CSS_SELECTOR, elem.addUserButton)

        self.assertIn(user_delete_toast, 'Successfully Deleted')
        self.assertTrue(add_user_button.is_displayed())

if __name__ == '__main__':
    unittest.main()
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

    def test_add_user_functionality(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()

        driver.find_element(By.CSS_SELECTOR, elem.adminButton).click()
        driver.find_element(By.CSS_SELECTOR, elem.addUserButton).click()

        driver.find_element(By.CSS_SELECTOR, elem.userRoleDropdown).click()
        driver.find_element(By.CSS_SELECTOR, elem.roleEssOption).click()
        driver.find_element(By.CSS_SELECTOR, elem.statusDropdown).click()
        driver.find_element(By.CSS_SELECTOR, elem.statusEnabledOption).click()
        driver.find_element(By.CSS_SELECTOR, elem.employeeNameInput).send_keys('s')
        driver.find_element(By.CSS_SELECTOR, elem.employeeNameOption).click()
        driver.find_element(By.CSS_SELECTOR, elem.usernameInput).send_keys(inputan.username)
        driver.find_element(By.CSS_SELECTOR, elem.passwordInput).send_keys(inputan.password)
        driver.find_element(By.CSS_SELECTOR, elem.confirmPasswordInput).send_keys(inputan.password)
        driver.find_element(By.CSS_SELECTOR, elem.addUserSaveButton).click()
        toast = driver.find_element(By.CSS_SELECTOR, elem.addUserToastMessage)

        self.assertTrue(toast)

if __name__ == '__main__':
    unittest.main()
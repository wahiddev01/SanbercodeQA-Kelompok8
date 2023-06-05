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

import baseLogin

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_login_form_appear(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        login_form = driver.find_element(By.CSS_SELECTOR, elem.loginForm)
        self.assertTrue(login_form.is_displayed())

    def test_failed_login_empty_pass(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.invalidUser)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        error_message = driver.find_element(By.CSS_SELECTOR, elem.errorMessage).text

        self.assertIn(inputan.reqPass, error_message)

    def test_success_login_with_input(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, inputan.baseUrl + "/web/index.php/dashboard/index")

    def test_success_logout(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        baseLogin.test_success_login(driver)
        driver.find_element(By.CSS_SELECTOR, elem.profilAvatar).click()
        driver.find_element(By.CSS_SELECTOR, elem.logoutButton).click()
        login_title = driver.find_element(By.CSS_SELECTOR, elem.loginTitle)
        self.assertTrue(login_title.is_displayed())

    def test_forget_password_appear(self):
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get(inputan.baseUrl)
        driver.find_element(By.CSS_SELECTOR, elem.forgotPasswordButton).click()
        reset_pwd_title = driver.find_element(By.CSS_SELECTOR, elem.resetPasswordTitle)
        self.assertTrue(reset_pwd_title.is_displayed())

if __name__ == '__main__':
    unittest.main()
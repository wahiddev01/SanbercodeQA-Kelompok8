import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append('../ElementLocator')
sys.path.append('../DataStorage')

from ElementLocator.locator import elem
from DataStorage.data import inputan

class TestUsers(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    # def test_edit_user_page(self):
    #     driver = self.browser
    #     driver.get(inputan.baseUrl)
    #     driver.implicitly_wait(10)
    #     driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
    #     driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
    #     driver.find_element(By.CLASS_NAME, elem.loginButton).click()

    #     driver.find_element(By.CSS_SELECTOR, elem.adminButton).click()
    #     driver.find_element(By.CSS_SELECTOR, elem.usersCellEditButton).click()
    #     edit_user_page_title = driver.find_element(By.CSS_SELECTOR, elem.editUserPageTitle)

    #     self.assertTrue(edit_user_page_title.is_displayed())

    def test_edit_user_functionality(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.implicitly_wait(10)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()

        driver.find_element(By.CSS_SELECTOR, elem.adminButton).click()

        driver.find_element(By.CSS_SELECTOR, elem.usersCellEditButton).click()
        driver.find_element(By.CSS_SELECTOR, elem.editUsernameInput).send_keys(inputan.editUsername)

        button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, elem.editSaveButton)))
        driver.execute_script("arguments[0].scrollIntoView();", button)
        button.click()

        toast = driver.find_element(By.CSS_SELECTOR, elem.editUserToastMessage)

        self.assertTrue(toast.is_displayed())

if __name__ == '__main__':
    unittest.main()
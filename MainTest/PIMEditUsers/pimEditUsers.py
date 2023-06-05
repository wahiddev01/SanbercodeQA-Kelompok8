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
    
    def test_edit_success_pim(self):
        
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.implicitly_wait(10000)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        driver.find_element(By.XPATH, elem.pimBtn).click()
        pimModule = driver.find_element(By.XPATH, elem.pimModule)

        self.assertTrue(pimModule.is_displayed())
        driver.find_element(By.XPATH, elem.fieldEmployee).send_keys("Amar")
        driver.find_element(By.XPATH, elem.btnSearch).click()
        driver.find_element(By.XPATH, elem.checkboxSearch).click()
        driver.find_element(By.XPATH, elem.btnEditPIM).click()
        driver.find_element(By.XPATH, elem.btnSaveEditPIM).click()
        success_message = driver.find_element(By.ID, elem.pimSuccessEditToast).text
        self.assertIn(success_message, 'Successfully Saved')

    def test_edit_success_pim_job(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.implicitly_wait(10000)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        driver.find_element(By.XPATH, elem.pimBtn).click()
        pimModule = driver.find_element(By.XPATH, elem.pimModule)

        self.assertTrue(pimModule.is_displayed())
        driver.find_element(By.XPATH, elem.fieldEmployee).send_keys("Amar")
        driver.find_element(By.XPATH, elem.btnSearch).click()
        driver.find_element(By.XPATH, elem.checkboxSearch).click()
        driver.find_element(By.XPATH, elem.btnEditPIM).click()
        driver.find_element(By.XPATH, elem.btnSubMenuJob).click()
        success_message = driver.find_element(By.ID, elem.pimSuccessEditToast).text
        self.assertIn(success_message, 'Successfully Saved')

    def test_edit_success_pim_salary(self):
        driver = self.browser
        driver.get(inputan.baseUrl)
        driver.implicitly_wait(10000)
        driver.find_element(By.CSS_SELECTOR, elem.username).send_keys(inputan.validUser)
        driver.find_element(By.CSS_SELECTOR, elem.password).send_keys(inputan.validPass)
        driver.find_element(By.CLASS_NAME, elem.loginButton).click()
        driver.find_element(By.XPATH, elem.pimBtn).click()
        pimModule = driver.find_element(By.XPATH, elem.pimModule)

        self.assertTrue(pimModule.is_displayed())
        driver.find_element(By.XPATH, elem.fieldEmployee).send_keys("Amar")
        driver.find_element(By.XPATH, elem.btnSearch).click()
        driver.find_element(By.XPATH, elem.checkboxSearch).click()
        driver.find_element(By.XPATH, elem.btnEditPIM).click()
        driver.find_element(By.XPATH, elem.btnSubMenuSalary).click()
        driver.find_element(By.XPATH, elem.btnEditSalary).click()
        driver.find_element(By.XPATH, elem.fieldSalaryComponents).send_keys("Test")
        driver.find_element(By.XPATH, elem.fieldAmount).send_keys("1000000")
        success_message = driver.find_element(By.ID, elem.pimSuccessEditToast).text
        self.assertIn(success_message, 'Successfully Saved')





if __name__ == '__main__':
    unittest.main()
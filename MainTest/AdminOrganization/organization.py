import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import sys
sys.path.append("../..")
sys.path.append("../LoginLogout")
import baseLogin
from ElementLocator.locators import el

class TestDeleteUser(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        sleep(3)
        self.browser.close()

    def test_TC018(self):
        print("TC018")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.XPATH, el.orgMenu).click()
        driver.find_element(By.XPATH, el.genInfo).click()
        genInfoForm = driver.find_element(By.XPATH, el.genInfoForm)
        self.assertTrue(genInfoForm.is_displayed)
    
    def test_TC019(self):
        print("TC019")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.XPATH, el.orgMenu).click()
        driver.find_element(By.XPATH, el.locations).click()
        locSearch = driver.find_element(By.XPATH, el.locSearch)
        self.assertTrue(locSearch.is_displayed)
    
    def test_TC020(self):
        print("TC020")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.XPATH, el.orgMenu).click()
        driver.find_element(By.XPATH, el.locations).click()
        locList = driver.find_element(By.XPATH, el.locList)
        self.assertTrue(locList.is_displayed)

    def test_TC021(self):
        print("TC021")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.XPATH, el.orgMenu).click()
        driver.find_element(By.XPATH, el.structure).click()
        orgStructure = driver.find_element(By.XPATH, el.orgStructure)
        self.assertTrue(orgStructure.is_displayed)

if __name__ == "__main__":
    unittest.main()
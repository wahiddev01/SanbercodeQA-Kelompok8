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
from DataStorage.datas import datas
from ElementLocator.locators import el

class TestDeleteUser(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        sleep(3)
        self.browser.close()
    
    def test_TC015(self):
        print("TC015")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.trashIco).click()
        driver.find_element(By.XPATH, el.confDelBtn).click()
        deleteMessage = driver.find_element(By.XPATH, el.deleteMessage).text
        self.assertIn(datas.deleteMessage, deleteMessage)
    
    def test_TC016(self):
        print("TC016")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.trashIco).click()
        driver.find_element(By.XPATH, el.cancDelBtn).click()
        currentUrl = driver.current_url
        self.assertIn(datas.userListUrl, currentUrl)
    
    def test_TC017(self):
        print("TC017")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.trashIco).click()
        driver.find_element(By.CLASS_NAME, el.closeBtn).click()
        currentUrl = driver.current_url
        self.assertIn(datas.userListUrl, currentUrl)

if __name__ == "__main__":
    unittest.main()
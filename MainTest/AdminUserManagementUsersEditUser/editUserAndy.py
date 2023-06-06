import unittest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import sys
sys.path.append("../..")
sys.path.append("../LoginLogout")
import baseLogin
from DataStorage.datas import datas
from ElementLocator.locators import el

class TestEditUser(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option('detach', True)
        self.browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        sleep(3)
        self.browser.close()

    def test_TC001(self):
        print("TC001")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        driver.find_element(By.XPATH, el.userRole).click()
        driver.find_element(By.XPATH, el.validRole).click()
        driver.find_element(By.XPATH, el.saveBtn).click()
        sleep(2)
        successMessage = driver.find_element(By.XPATH, el.savedMessage).text
        self.assertIn(datas.successMessage, successMessage)
    
    def test_TC002(self):
        print("TC002")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        inputEmplName = driver.find_element(By.XPATH, el.emplName)
        inputEmplName.send_keys(Keys.CONTROL + "a")
        inputEmplName.send_keys(Keys.DELETE)
        inputEmplName.send_keys(datas.emplName)
        driver.find_element(By.XPATH, el.validEmplName).click()
        driver.find_element(By.XPATH, el.saveBtn).click()
        successMessage = driver.find_element(By.XPATH, el.savedMessage).text
        self.assertIn(datas.successMessage, successMessage)

    def test_TC003(self):
        print("TC003")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        driver.find_element(By.XPATH, el.status).click()
        driver.find_element(By.XPATH, el.validStatus).click()
        driver.find_element(By.XPATH, el.saveBtn).click()
        sleep(2)
        successMessage = driver.find_element(By.XPATH, el.savedMessage).text
        self.assertIn(datas.successMessage, successMessage)
    
    def test_TC004(self):
        print("TC004")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        inputUsername = driver.find_element(By.XPATH, el.username)
        sleep(1)
        inputUsername.send_keys(Keys.CONTROL + "a")
        inputUsername.send_keys(Keys.DELETE)
        inputUsername.send_keys(datas.username)
        driver.find_element(By.XPATH, el.saveBtn).click()
        sleep(2)
        successMessage = driver.find_element(By.XPATH, el.savedMessage).text
        self.assertIn(datas.successMessage, successMessage)
    
    def test_TC005(self):
        print("TC005")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        driver.find_element(By.XPATH, el.passCBox).click()
        driver.find_element(By.XPATH, el.newPass).send_keys(datas.newPass)
        driver.find_element(By.XPATH, el.confPass).send_keys(datas.confPass)
        driver.find_element(By.XPATH, el.saveBtn).click()
        sleep(2)
        successMessage = driver.find_element(By.XPATH, el.savedMessage).text
        self.assertIn(datas.successMessage, successMessage)

    def test_TC006(self):
        print("TC006")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        driver.find_element(By.XPATH, el.cancelBtn).click()
        currentUrl = driver.current_url
        self.assertIn(datas.userListUrl, currentUrl)
    
    def test_TC007(self):
        print("TC007")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        driver.find_element(By.XPATH, el.userRole).click()
        driver.find_element(By.XPATH, el.invalidRole).click()
        driver.find_element(By.XPATH, el.saveBtn).click()
        requiredMessage = driver.find_element(By.XPATH, el.requiredMessage).text
        self.assertIn(datas.reqMessage, requiredMessage)
    
    def test_TC008(self):
        print("TC008")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        inputEmplName = driver.find_element(By.XPATH, el.emplName)
        inputEmplName.send_keys(Keys.CONTROL + "a")
        inputEmplName.send_keys(Keys.DELETE)
        inputEmplName.send_keys(datas.invalidEmplName)
        driver.find_element(By.XPATH, el.saveBtn).click()
        invalidMessage = driver.find_element(By.XPATH, el.invalidMessage).text
        self.assertIn(datas.invalidMessage, invalidMessage)
    
    def test_TC009(self):
        print("TC009")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        inputEmplName = driver.find_element(By.XPATH, el.emplName)
        inputEmplName.send_keys(Keys.CONTROL + "a")
        inputEmplName.send_keys(Keys.DELETE)
        inputEmplName.send_keys(datas.blank)
        driver.find_element(By.XPATH, el.saveBtn).click()
        requiredMessage = driver.find_element(By.XPATH, el.requiredMessage).text
        self.assertIn(datas.reqMessage, requiredMessage)

    def test_TC010(self):
        print("TC010")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        driver.find_element(By.XPATH, el.status).click()
        driver.find_element(By.XPATH, el.invalidStatus).click()
        driver.find_element(By.XPATH, el.saveBtn).click()
        requiredMessage = driver.find_element(By.XPATH, el.requiredMessage).text
        self.assertIn(datas.reqMessage, requiredMessage)
    
    def test_TC011(self):
        print("TC011")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        inputUsername = driver.find_element(By.XPATH, el.username)
        sleep(1)
        inputUsername.send_keys(Keys.CONTROL + "a")
        inputUsername.send_keys(Keys.DELETE)
        inputUsername.send_keys(datas.blank)
        driver.find_element(By.XPATH, el.saveBtn).click()
        requiredMessage = driver.find_element(By.XPATH, el.requiredMessage).text
        self.assertIn(datas.reqMessage, requiredMessage)

    def test_TC012(self):
        print("TC012")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        inputUsername = driver.find_element(By.XPATH, el.username)
        sleep(1)
        inputUsername.send_keys(Keys.CONTROL + "a")
        inputUsername.send_keys(Keys.DELETE)
        inputUsername.send_keys(datas.lessUsername)
        driver.find_element(By.XPATH, el.saveBtn).click()
        lessCharMessage = driver.find_element(By.XPATH, el.lessCharMessage).text
        self.assertIn(datas.lessCharMessage, lessCharMessage)

    def test_TC013(self):
        print("TC013")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        driver.find_element(By.XPATH, el.passCBox).click()
        driver.find_element(By.XPATH, el.saveBtn).click()
        requiredPass = driver.find_element(By.XPATH, el.requiredPass).text
        self.assertIn(datas.reqMessage, requiredPass)
        requiredConfPass = driver.find_element(By.XPATH, el.requiredConfPass).text
        self.assertIn(datas.reqMessage, requiredConfPass)

    def test_TC014(self):
        print("TC014")
        driver = self.browser
        driver.maximize_window()
        driver.implicitly_wait(20)
        baseLogin.test_success_login(driver)
        driver.find_element(By.XPATH, el.adminMenu).click()
        driver.find_element(By.CLASS_NAME, el.pencilIco).click()
        driver.find_element(By.XPATH, el.passCBox).click()
        driver.find_element(By.XPATH, el.newPass).send_keys(datas.newPass)
        driver.find_element(By.XPATH, el.confPass).send_keys(datas.invalidConfPass)
        driver.find_element(By.XPATH, el.saveBtn).click()
        notMatchPass = driver.find_element(By.XPATH, el.notMatchPass).text
        self.assertIn(datas.notMatchPass, notMatchPass)

if __name__ == "__main__":
    unittest.main()
import unittest
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import baselogin

class TestPIMAdd(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
    
    def test_TC13(self): #Add Employee Success
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "middleName").send_keys("Sri")
        driver.find_element(By.NAME, "lastName").send_keys("jabbar")
        driver.find_element(By.CLASS_NAME, "employee-image").click()
        time.sleep(3)
        pyautogui.write(r"D:\QA - Sanbercode\FinalProject\SanbercodeQA-Kelompok8\MainTest\PIMEmployeeListAddEmployee\profilepicture.png")
        pyautogui.press("enter")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    def test_TC14(self): #Add Employee with Empty First Name Fail
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("")
        driver.find_element(By.NAME, "middleName").send_keys("Sri")
        driver.find_element(By.NAME, "lastName").send_keys("Jabbar")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
        self.assertIn("Required", error_message)
        time.sleep(3)

    def test_TC15(self): #Add Employee with Empty Last Name Fail
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "middleName").send_keys("Sri")
        driver.find_element(By.NAME, "lastName").send_keys("")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']").text
        self.assertIn("Required", error_message)
        time.sleep(3)

    def test_TC16(self): #Add Employee Fail Invalid Photo
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "middleName").send_keys("Sri")
        driver.find_element(By.NAME, "lastName").send_keys("jabbar")
        driver.find_element(By.CLASS_NAME, "employee-image").click()
        time.sleep(3)
        pyautogui.write(r"D:\QA - Sanbercode\FinalProject\SanbercodeQA-Kelompok8\MainTest\PIMEmployeeListAddEmployee\profilepictureinvalid.pdf")
        pyautogui.press("enter")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_TC17(self): #Add Employee with create login details sukses
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "middleName").send_keys("Sri")
        driver.find_element(By.NAME, "lastName").send_keys("Jabbar")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span"
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input"
            ).send_keys("srijabbbbar")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
            ).send_keys("Sripassword1")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
            ).send_keys("Sripassword1")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def test_TC18(self): #Add Employee with Invalid Username
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "middleName").send_keys("Sri")
        driver.find_element(By.NAME, "lastName").send_keys("Jabbar")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span"
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input"
            ).send_keys("srie")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
            ).send_keys("Sripassword1")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
            ).send_keys("Sripassword1")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div/span[.='Should be at least 5 characters']").text
        self.assertIn("Should be at least 5 characters", error_message)
        time.sleep(3)
        time.sleep(3)

    def test_TC19(self): #Add Employee with Invalid Password
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "middleName").send_keys("Sri")
        driver.find_element(By.NAME, "lastName").send_keys("Jabbar")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span"
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input"
            ).send_keys("srijabbbbar")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
            ).send_keys("Huddddaaaa")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
            ).send_keys("Huddddaaaa")
        time.sleep(6)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div/span[.='Your password must contain minimum 1 number']").text
        self.assertIn("Your password must contain minimum 1 number", error_message)
        time.sleep(3)

    def test_TC20(self): #Add Employee Invalid Confirm Password
        baseUrl = "https://opensource-demo.orangehrmlive.com/"
        driver = self.browser 
        driver.get(baseUrl) 
        baselogin.test_success_login(driver)
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/dashboard/index")
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//aside[@class='oxd-sidepanel']/nav[@role='navigation']//ul[@class='oxd-main-menu']//a[@href='/web/index.php/pim/viewPimModule']/span[.='PIM']",
        ).click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/viewEmployeeList")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        currentUrl = driver.current_url
        self.assertIn (currentUrl, baseUrl + "web/index.php/pim/addEmployee")
        time.sleep(3)
        driver.find_element(By.NAME, "firstName").send_keys("John")
        driver.find_element(By.NAME, "middleName").send_keys("Sri")
        driver.find_element(By.NAME, "lastName").send_keys("Jabbar")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']//form[@class='oxd-form']//div[@class='oxd-form-row user-form-header']/div[@class='oxd-switch-wrapper']//span"
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='orangehrm-employee-form']/div[3]/div/div[1]/div//input"
            ).send_keys("srijabbbbar")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters user-password-cell']/div//input[@type='password']"
            ).send_keys("Sripassword1")
        driver.find_element(
            By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div//input[@type='password']"
            ).send_keys("Sripassword11111")
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//form[@class='oxd-form']//div[@class='oxd-form-row user-password-row']/div/div[@class='oxd-grid-item oxd-grid-item--gutters']/div/span[.='Passwords do not match']").text
        self.assertIn("Passwords do not match", error_message)
        time.sleep(3)

    #reupload github
if __name__ == '__main__':
    unittest.main()
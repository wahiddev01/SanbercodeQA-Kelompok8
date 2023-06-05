import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import baselogin


class EmployeeListPIM(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_TC01(self): #Search by Employee Name found positive
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//input[@placeholder='Type for hints...']",).send_keys("sri")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[3]/div[.='John Jabbar']").text
        self.assertIn("John Jabbar", valid_message)
        time.sleep(3)
    
    def test_TC02(self): #Search by Employee ID found positive
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]//input",
            ).send_keys("EMP0001")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[2]/div[.='EMP0001']").text
        self.assertIn("EMP0001", valid_message)
        time.sleep(3)

    def test_TC03(self): #Search by Employment Status found positive
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[3]/div//div[@class='oxd-select-text-input']",
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div[2]/div[5]/span",
            ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]//div[@role='row']/div[6]/div[.='Full-Time Probation']").text
        self.assertIn("Full-Time Probation", valid_message)
        time.sleep(3)

    def test_TC04(self): #Search By Include found positive
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[4]/div//div[@class='oxd-select-text-input']",
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/span",
            ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[1]/div[@role='row']/div[9]").text
        self.assertIn("Actions", valid_message)
        time.sleep(3)

    def test_TC05(self): #Search by Supervisor Name
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]/div//input[@placeholder='Type for hints...']",
            ).send_keys("ram")
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, "oxd-autocomplete-option").click()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[1]/div[@role='row']/div[9]").text
        self.assertIn("Actions", valid_message)
        time.sleep(2)

    def test_TC06(self): #Search by Job Title
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[6]/div//div[@class='oxd-select-text-input']",
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[6]/div/div[2]/div/div[2]/div[17]/span",
            ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[5]/div[.='Payroll Administrator']").text
        self.assertIn("Payroll Administrator", valid_message)
        time.sleep(3)

    def test_TC07(self): #Search by Sub Unit Success
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[7]/div//div[@class='oxd-select-text-input']",
            ).click()
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]/div/div[2]/div/div[2]/div[6]/span",
            ).click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[2]/div[1]/div[@role='row']/div[7]/div[.='Administration']").text
        self.assertIn("Administration", valid_message)
        time.sleep(3)

    def test_TC08(self): #TC08 Reset Filter Success
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//input[@placeholder='Type for hints...']",).send_keys("sri")
        driver.find_element(By.XPATH, "//button[@type='reset']").click()
        time.sleep(2)
    
    def test_TC09(self): #Search Invalid Name Negative Result
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//input[@placeholder='Type for hints...']",).send_keys("kerupuk")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text
        self.assertIn("No Records Found", error_message)
        time.sleep(3)

    def test_TC10(self): #Search Blank Name Negative Result
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//input[@placeholder='Type for hints...']",).clear()
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        valid_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']//div[@role='table']/div[1]/div[@role='row']/div[9]").text
        self.assertIn("Actions", valid_message)
        time.sleep(3)

    def test_TC11(self): #Search Invalid ID
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[2]//input",
            ).send_keys("000")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(3)
        error_message = driver.find_element(By.XPATH, "//div[@id='app']/div[@class='oxd-layout']/div[@class='oxd-layout-container']/div[@class='oxd-layout-context']//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']/span[@class='oxd-text oxd-text--span']").text
        self.assertIn("No Records Found", error_message)
        time.sleep(3)

    def test_TC12(self): #Searcy by Supervisor name but invalid name
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
        time.sleep(3)
        driver.find_element(
            By.XPATH,
            "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]/div//input[@placeholder='Type for hints...']",
            ).send_keys("botol")
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(5)
        error_message = driver.find_element(By.XPATH, "//div[@id='app']//div[@class='oxd-table-filter']/div[@class='oxd-table-filter-area']/form[@class='oxd-form']/div[@class='oxd-form-row']/div/div[5]/div/span[.='Invalid']").text
        self.assertIn("Invalid", error_message)
        time.sleep(2)

#reupload github
if __name__ == '__main__':
    unittest.main()
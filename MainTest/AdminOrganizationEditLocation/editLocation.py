import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.append('../../')
import ElementLocator.elements as E

class TestEditLocation(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_edit_Location(self):
        driver = self.browser
        driver.get(E.element.url)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
        driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
        driver.find_element(By.XPATH, E.element.btnlogin).click()
      #   driver.implicitly_wait(10)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
      #   currentUrl = driver.current_url
      #   self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.editSelected))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.titleEditValidasi ))).text

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhname))).send_keys("Kota Maju Jaya")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnsave))).click()
        successMessage = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"))).get_attribute("innerHTML")
        self.assertIn("Successfully Updated", successMessage)
    
    def test_success_edit_city(self):
        driver = self.browser
        driver.get(E.element.url)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
        driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
        driver.find_element(By.XPATH, E.element.btnlogin).click()
      
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
      
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.editSelected))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.titleEditValidasi ))).text

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcity))).send_keys("City Baru")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnsave))).click()
        successMessage = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"))).get_attribute("innerHTML")
        self.assertIn("Successfully Updated", successMessage)
    
      

    def test_failededit_requiredName(self):
        driver = self.browser
        driver.get(E.element.url)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
        driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
        driver.find_element(By.XPATH, E.element.btnlogin).click()
    
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.editSelected))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.titleEditValidasi ))).text
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhname))).send_keys(" ")
        name = driver.find_element(By.XPATH, E.element.mhname)
        
        name.send_keys(Keys.CONTROL+"a")
        name.send_keys(Keys.DELETE)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnsave))).click()
        errorMessage = driver.find_element(By.XPATH, E.element.requiredField).get_attribute("innerHTML")
        self.assertIn("Required", errorMessage)
       

    def test_failedit_requiredCountry(self):
        driver = self.browser
        driver.get(E.element.url)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
        driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
        driver.find_element(By.XPATH, E.element.btnlogin).click()
      #   driver.implicitly_wait(10)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
      #   currentUrl = driver.current_url
      #   self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.editSelected))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.titleEditValidasi ))).text

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcountry))).send_keys(" ")
        driver.find_element(By.XPATH, E.element.btnsave).click()
    

    def test_cancel_edit_Location(self):
        driver = self.browser
        driver.get(E.element.url)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
        driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
        driver.find_element(By.XPATH, E.element.btnlogin).click()
      #   driver.implicitly_wait(10)
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
      #   currentUrl = driver.current_url
      #   self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.editSelected))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.titleEditValidasi ))).text
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnCancel))).click()
        currentUrl = driver.current_url
        self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")

if __name__ == '__main__':
    unittest.main()
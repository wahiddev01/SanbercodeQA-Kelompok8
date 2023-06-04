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

class TestDeleteLocations(unittest.TestCase):
     def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())
     
     def test_success_delete_Location(self):
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
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.deleteSelected))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.popUpyes))).click()

        successMessage = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"))).get_attribute("innerHTML")
        self.assertIn("Successfully Deleted", successMessage)

        # delete_message =  driver.find_elements(By.XPATH, E.element.messageDelete)
        # self.assertIn("Successfully Deleted", delete_message)
        currentUrl = driver.current_url
        self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")

     def test_cancel_delete_Location(self):
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
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.deleteSelected))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.popUpNo))).click()
        
        currentUrl = driver.current_url
        self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")

if __name__ == '__main__':
    unittest.main()
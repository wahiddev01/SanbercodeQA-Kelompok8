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

import sys
sys.path.append('../')


class TestFailAddLocations(unittest.TestCase):
     def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

     def test_fail_requiredName(self):
        
         driver = self.browser
         driver.get(E.element.url)
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
         driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
         driver.find_element(By.XPATH, E.element.btnlogin).click()
      #   defaultLogin
      #   driver.implicitly_wait(10)
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
         currentUrl = driver.current_url
         self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnAdd))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcity))).send_keys("South Florida")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhprovince))).send_keys("US")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhzipcode))).send_keys("1111")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcountry))).send_keys("United States")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnotelp))).send_keys("088881122")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhfax))).send_keys("0109876")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhaddress))).send_keys("Kemenangan")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnote))).send_keys("New Add")
         driver.find_element(By.XPATH, E.element.btnsave).click()
         errorMessage = driver.find_element(By.XPATH, E.element.requiredField).get_attribute("innerHTML")
         self.assertIn("Required", errorMessage)

     def test_fail_requiredCountry(self):
         driver = self.browser
         driver.get(E.element.url)
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
         driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
         driver.find_element(By.XPATH, E.element.btnlogin).click()
      #   defaultLogin
      #   driver.implicitly_wait(10)
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
         currentUrl = driver.current_url
         self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnAdd))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcountry))).send_keys("United St")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcity))).send_keys("South Florida")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhprovince))).send_keys("US")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhzipcode))).send_keys("1111")
         
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnotelp))).send_keys("088881122")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhfax))).send_keys("0109876")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhaddress))).send_keys("Kemenangan")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnote))).send_keys("New Add")
         errorMessage = driver.find_element(By.XPATH, E.element.requiredField).get_attribute("innerHTML")
         self.assertIn("Required", errorMessage)

if __name__ == '__main__':
    unittest.main()
       
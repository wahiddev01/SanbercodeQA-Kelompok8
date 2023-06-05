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

# import sys
# sys.path.append('../')
# import defaultLogin as defaultLogin

class TestAddLocations(unittest.TestCase):
     def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

     def test_success_Add_Location(self):
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
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhname))).send_keys("Kota Maju")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcity))).send_keys("Bandung")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhprovince))).send_keys("Jawa Barat")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhzipcode))).send_keys("43251")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcountry))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnotelp))).send_keys("089812345")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhfax))).send_keys("021345678")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhaddress))).send_keys("Jalan Raya")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnote))).send_keys("New Add")

        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnsave))).click()
        successMessage = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"))).get_attribute("innerHTML")
        self.assertIn("Successfully Saved", successMessage)
     
     def test_success_Add_Location_blankCity(self):
         driver = self.browser
         driver.get(E.element.url)
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
         driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
         driver.find_element(By.XPATH, E.element.btnlogin).click()
      #    defaultLogin
      #   driver.implicitly_wait(10)
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
         currentUrl = driver.current_url
         self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnAdd))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhname))).send_keys("South Florida")
       
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhprovince))).send_keys("US")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhzipcode))).send_keys("1111")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcountry))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]"))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnotelp))).send_keys("088881122")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhfax))).send_keys("0109876")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhaddress))).send_keys("Kemenangan")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnote))).send_keys("New Add")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnsave))).click()
         successMessage = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"))).get_attribute("innerHTML")
         self.assertIn("Successfully Saved", successMessage)
   
          
     def test_success_Add_Location_blankProvince(self):
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
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhname))).send_keys("North Florida")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcity))).send_keys("Mexico")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhzipcode))).send_keys("1112")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhcountry))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[2]/div[2]"))).click()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnotelp))).send_keys("088881125")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhfax))).send_keys("01098798")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhaddress))).send_keys("Kemenangan Jaya")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhnote))).send_keys("New Add")
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnsave))).click()
      
        successMessage = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-text--toast-message oxd-toast-content-text']"))).get_attribute("innerHTML")
        self.assertIn("Successfully Saved", successMessage)
    
     def test_cancel_add(self):
         driver = self.browser
         driver.get(E.element.url)
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.mhusername))).send_keys("Admin")
         driver.find_element(By.XPATH, E.element.mhpass).send_keys("admin123")
         driver.find_element(By.XPATH, E.element.btnlogin).click()
      # 
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.navbarAdmin))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.menuOrganization))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.location))).click()
         currentUrl = driver.current_url
         self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnAdd))).click()
         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, E.element.btnCancel))).click()
         currentUrl = driver.current_url
         self.assertIn(currentUrl, E.element.url  +"web/index.php/admin/viewLocations.html")

if __name__ == '__main__':
    unittest.main()
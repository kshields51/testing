import unittest
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time

class GoogleSearch(unittest.TestCase):
    
    def setup(self):
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\kshie\Documents\testing\selenium-drivers\geckodriver.exe") # needed to download the geckodriver
        '''This timeout is used to specify the amount of time the driver should wait while searching for an element if it is not immediately present. https://www.browserstack.com/guide/understanding-selenium-timeouts'''
        self.driver.implicitly_wait(30)
        self.base_url = "https://ecpat.org/join-ecpat/ "

    def test_google_search(self):
        driver = self.driver 
        driver.get(self.base_url) # There is a chance that the site blocks you if the program fails out here saying its taking to long to respond

        element = driver.find_element_by_id("Enter-your-email-address-2")
        print("looking for q")
        element.clear()
        element.send_keys("Selenium testing tools cookbook")
        time.sleep(10) # lol it worked
        element.submit()

        WebDriverWait(driver, 30).until(expected_conditions.title_contains("Selenium testing tools cookbook"))
        self.assertEqual(driver.title, "Selenium testing tools cookbook - Google Search")
    
    def tearDown(self):
        self.driver.quit()
    
if __name__ == "__main__":
    unittest.main(verbosity=2, warnings="ignore")
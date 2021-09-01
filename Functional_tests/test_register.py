
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.test.testcases import TransactionTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from accounts.models import Customer
from selenium import webdriver
from selenium.webdriver.common.by import By



class testing_login(TransactionTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome("/home/mihlali/Downloads\chromedriver.exe")
        self.browser.get("http://127.0.0.1:8000/login/?next=/")
        
    
    def testing_register(self):
        self.regLink = self.browser.find_element_by_class_name("ml-2")
        
        self.regLink.click()
        try:



            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "id_username")))
            self.username.send_keys("hectic")
            self.email = self.browser.find_element_by_id("id_email")
            self.email.send_keys("hectic@gmail.com")
            self.password1 = self.browser.find_element_by_id("id_password1")
            self.password1.send_keys("hectic")
            self.password2 = self.browser.find_element_by_id("id_password2")
            self.password2.send_keys("hectic")
            
        except Exception as err:
            print(err)
        
        try:


            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)

    def test_login(self):
        try:
            self.username = WebDriverWait(self.browser, 50).until(EC.presence_of_element_located((By.ID, "username")))
            self.username.send_keys("hectic")
            self.password = self.browser.find_element_by_id("password")
            self.password.send_keys("hectic")
            
        except Exception as err:
            print(err)

        try:
            self.registerButton = self.browser.find_element_by_class_name("btn")
            self.registerButton.click()
        except Exception as err:
            print(err)
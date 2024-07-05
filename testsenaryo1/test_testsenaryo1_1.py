
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

  

# Test Senaryosu 1 (Otel Ara İşlemi)
# Case 1 : Tatil arama alanında  bir çocuğun yaşı  seçildiğinde uyarı mesajının gösterilmesi.

class TestOtelAraİslemi():     

    def setup_method(self):
                
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.tatilsepeti.com/")


    def teardown_method(self):        
        self.driver.quit()

    def test_otelaraislemi(self):
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "bolge"))).send_keys("Antalya")
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='ui-id-5']/span"))).click()
        sleep(6)
        giris_tarihi_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "giris-tarihi")))
        giris_tarihi_input.click()
        
        tarih_gun = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "22")))
        tarih_gun.click()
        
        cikis_tarihi_input = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.ID, "cikis-tarihi")))
        time.sleep(10)
        cikis_tarihi_input.click()
        sleep(6)
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "25"))).click()
        sleep(5)
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='oda_1']/div/div/div/div/div/div/i"))).click()
        sleep(2)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='oda_1']/div/div/div/div[2]/div/div/i"))).click()
        sleep(8)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='childAge_1_1']/option[14]"))).click()
        sleep(5)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.ID, "searchBtn"))).click()
        sleep(2)

    
        
       
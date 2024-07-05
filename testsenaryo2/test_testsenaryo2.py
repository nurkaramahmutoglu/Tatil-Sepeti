
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
 

# Test Senaryosu 2 (Rezervasyon Yönetimi)

class TestRezervasyon():

    def setup_method(self):
        
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
       
        self.driver.quit()

    @pytest.mark.case1
    def test_case1(self):
        # Case 1: Yapılan Rezervasyonun Detaylarının Görüntülenmesi Ve Uyarı Mesajı Alması
        self.driver.get("https://www.tatilsepeti.com/")
       
        
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

    def test_case2(self):
        # Case 2: Arama Sonucu Listenenlerden Bir Tanesinin Seçilmesi
        self.driver.get("https://www.tatilsepeti.com/oneri-listesi/?query=antalya&ara=oda:1-13;tarih:22.07.2024,25.07.2024;click:true")
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.LINK_TEXT, "Antalya"))).click()
        
        
    @pytest.mark.case3
    def test_case3(self):
        # Case 3: Başarılı Antalya Otellerin Listelenmesi ve "Regnum Carya" otelin detaylarına tıklanması
        self.driver.get("https://www.tatilsepeti.com/antalya-otelleri?ara=oda:1-13;tarih:22.07.2024,25.07.2024;click:true")
        self.driver.execute_script("window.scrollTo(0,400);") # bak
        sleep(1)
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "(//a[contains(text(),'Detayları İncele')])[2]"))).click()
    
    @pytest.mark.case5 
    @pytest.mark.case4
    def test_case4_case5(self):
        # Case 4: Rezervasyonun Düzenlenmesi (Tarih Değişikliği Yapılması)
        # Case 5: Birden Fazla Kişi için Rezervasyon Yapılması
        self.driver.get("https://www.tatilsepeti.com/regnum-carya?ara=oda:1-13;tarih:22.07.2024,25.07.2024")
        self.driver.execute_script("window.scrollTo(0,500);") 
        time.sleep(3)        
        giris_tarihi_input = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "startDateDetail")))
        giris_tarihi_input.click()         
        tarih_gun = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "1")))
        tarih_gun.click()
        sleep(1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "12"))).click()     
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".pax-info-wrapper"))).click()
        sleep(5)       
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "detailDateUpdateBtn"))).click()
        sleep(5)        
        time.sleep(5)
        
    @pytest.mark.case6
    def test_case6(self): 
        # Case 6: Başarılı Rezervasyon Yap Butonuna Tıklama (Amber Lagoon Suite)
        self.driver.get("https://www.tatilsepeti.com/regnum-carya?ara=oda:3-13;tarih:01.08.2024,12.08.2024")
        self.driver.execute_script("window.scrollTo(0,500);")
        sleep(2)
        
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located((By.XPATH, "//div[@id='dev-roomList']/div[9]/aside/div[2]/div/div[2]/div[3]/button"))).click()
    
    @pytest.mark.case7
    def test_case7(self):
        # Case 7 : Başarılı Misafir Bilgilerinin Kaydedilmesi
        self.driver.get("https://www.tatilsepeti.com/reservation/hotelreservation?id=J0bE9u7a0XGrVjuQhwrGaX%2FjnzhbWToKyHAbsVaddxS5cebA7PbkalS2aNB5NuEvMiaHpNq8Mw39lZ%2B3q%2BRGjpEDRvevwgDb5xUmmK6Q1mbiyeudhi8WjxxS8G3XdUCQ")
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "ReservationViewModel_Contact_ContactGSM_AreaCityCode"))).send_keys("554")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "ReservationViewModel_Contact_ContactGSM_PhoneNumber"))).send_keys("1476532")
        sleep(5)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "ReservationViewModel_Contact_ContactEMail"))).send_keys("tatilsepetimin@gmail.com")  
        
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_0__Name"))).send_keys("Nur")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_0__SurName"))).send_keys("Kar")       
        
             
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_1__Name"))).send_keys("Buğlem")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_1__SurName"))).send_keys("Yılmaz")
        sleep(5)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_2__Name"))).send_keys("Sevda")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_2__SurName"))).send_keys("Yılmaz") 
        sleep(5)    
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_3__Name"))).send_keys("Çicek")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_3__SurName"))).send_keys("Yılmaz")     
        sleep(5)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "isValidateHotel"))).click()
    
    @pytest.mark.case8
    def test_case8(self):   
        #Case 8 : Başarısız Misafir Bilgilerinin Kaydedilmesi ( Eksik Harf Girme )
        self.driver.get("https://www.tatilsepeti.com/reservation/hotelreservation?id=J0bE9u7a0XGrVjuQhwrGaX%2FjnzhbWToKyHAbsVaddxS5cebA7PbkalS2aNB5NuEvMiaHpNq8Mw39lZ%2B3q%2BRGjpEDRvevwgDb5xUmmK6Q1mbiyeudhi8WjxxS8G3XdUCQ")
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "ReservationViewModel_Contact_ContactGSM_AreaCityCode"))).send_keys("554")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "ReservationViewModel_Contact_ContactGSM_PhoneNumber"))).send_keys("1476532")
        sleep(5)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "ReservationViewModel_Contact_ContactEMail"))).send_keys("tatilsepetimin@gmail.com")  
        
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_0__Name"))).send_keys("Nur")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_0__SurName"))).send_keys("Kar")       
        
             
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_1__Name"))).send_keys("Buğlem")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_1__SurName"))).send_keys("Yılmaz")
        sleep(5)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_2__Name"))).send_keys("Sevda")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_2__SurName"))).send_keys("Yılmaz") 
        sleep(5)    
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_3__Name"))).send_keys("Çicek")         
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "CustomerViewModel_3__SurName"))).send_keys("Y")     
        sleep(5)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "isValidateHotel"))).click()
   
    @pytest.mark.case9
    def test_case9(self):
        # Case 09 : Başarısız Rezervasyon Ödeme Alanında Kupon ya da İndirim Kodunu Girme Ve  Uyarı Mesajı Alması 
        # (Yanlış Girme)      
        self.driver.get("https://www.tatilsepeti.com/rezervasyonodeme?id=KSwaPNvZtVNXqDSdI0hn%2BHYx0BnnaChyzcdribioyFW4Z3dHLjsJaMLKSIQkWUdF")
        sleep(3)
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "couponsShowBtn"))).click() 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "campaignCouponCode"))).send_keys("7777777")
        sleep(3)     
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "couponBuyNowSp"))).click() 
        sleep(3) 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, "//button[@id='modalCloseCoupon']/span"))).click()
        sleep(3) 
        
    @pytest.mark.case10
    def test_case10(self):
        # Case 10 : Başarısız Kredi Kartı ile Güvenli Ödeme Ve Hatayı Kırmızı Renkte Göstermesi (Kart Numarasını Yanlış  Girme)
        self.driver.get("https://www.tatilsepeti.com/rezervasyonodeme?id=KSwaPNvZtVNXqDSdI0hn%2BHYx0BnnaChyzcdribioyFW4Z3dHLjsJaMLKSIQkWUdF")
       
        self.driver.execute_script("window.scrollTo(0,500);") 
        time.sleep(3) 
       
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "txtCardNumber"))).send_keys("7777  7777  7777  7777")
        sleep(3)     
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "PaymentViewModel_CreditCard_ExpireMonth"))).click()
        sleep(3) 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, "//option[. = '07']"))).click()
        sleep(3) 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "PaymentViewModel_CreditCard_ExpireYear"))).click()
        sleep(3) 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.XPATH, "//option[. = '2037']"))).click()
        sleep(3) 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "PaymentViewModel_CreditCard_CV2"))).send_keys("777")
        sleep(3) 
        
        self.driver.execute_script("window.scrollTo(0,200);") 
        time.sleep(3) 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "dev-paymentBtn"))).click()
        sleep(3) 
       
    @pytest.mark.case11
    def test_case11(self):
        # Case 10 : Başarısız Kredi Kartı ile Güvenli Ödeme Ve  Uyarı Mesajı Alması 
        # (Kart Numarası, Son Kullanma Tarihi ve CVC Numarasını Boş Bırakma)    
        self.driver.get("https://www.tatilsepeti.com/rezervasyonodeme?id=KSwaPNvZtVNXqDSdI0hn%2BHYx0BnnaChyzcdribioyFW4Z3dHLjsJaMLKSIQkWUdF")
         
        self.driver.execute_script("window.scrollTo(0,500);") 
        time.sleep(3) 
       
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "txtCardNumber"))).send_keys()
        sleep(3)     
            
        
        self.driver.execute_script("window.scrollTo(0,200);") 
        time.sleep(3) 
        WebDriverWait(self.driver,5).until(EC.visibility_of_element_located((By.ID, "dev-paymentBtn"))).click()
        sleep(3) 
       
        
       
        
        
       
        
       

      
       
      
    
    
    
        
        
       

        
        
        
        
       
          
        
       
  
         
         
        
       
        
        
       
        
       

      
       
      
    
    
    
        
        
       
        
        
       
        
       

      
       
      
    
    
    
        
        
       

       
     
        
        
       

        
        
        
        
        
   
       

 
        
      
       
        
   
       

 
        
    
    
        
        
       

        
        
        
        
        
   
       

 
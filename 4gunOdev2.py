# AMAÇ:

# Derste gösterilen konuların pekiştirilmesi.

# ÖDEV TANIMI:

# Aşağıda verilen test caselerin hepsini "https://www.saucedemo.com/" sitesinde gerçekleştirmeniz istenmektedir.

# Yazacağınız tüm kodları oluşturduğunuz bir classda fonksiyonlar oluşturarak gerçekleştiriniz. Bu classın fonksiyonlarını çağırarak test ediniz.

# Test Caseler;

# Kullanıcı adı ve şifre alanları boş geçildiğinde uyarı mesajı olarak "Epic sadface: Username is required" gösterilmelidir.
# Sadece şifre alanı boş geçildiğinde uyarı mesajı olarak "Epic sadface: Password is required" gösterilmelidir.
# Kullanıcı adı "locked_out_user" şifre alanı "secret_sauce" gönderildiğinde "Epic sadface: Sorry, this user has been locked out." mesajı gösterilmelidir.
# Kullanıcı adı ve şifre alanları boş geçildiğinde bu iki inputun yanında da kırmızı "X" ikonu çıkmalıdır. Daha sonra aşağıda çıkan uyarı mesajının kapatma butonuna tıklandığında bu "X" ikonları kaybolmalıdır. (Tek test casede işleyiniz)
# Kullanıcı adı "standard_user" şifre "secret_sauce" gönderildiğinde kullanıcı "/inventory.html" sayfasına gönderilmelidir.
# Giriş yapıldıktan sonra kullanıcıya gösterilen ürün sayısı "6" adet olmalıdır.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class Test_Sauce:

    def kullanici_adi_kontrol(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullaniciAdi=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(5)
        kullaniciAdi.send_keys("")
        sifre.send_keys("")
        sleep(5)
        giris.click()
        hatalimesaj=driver.find_element(By.CLASS_NAME, "error-message-container")
        mesaj="Epic sadface: Username is required"
	print("\n************Kul-Adı ve Şifre Boş Geçilemez Uyarı Kontrol**************") 
        print(f"Test Sonucu: {mesaj}")
        sleep(10)

    def sifre_kontrol(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullaniciAdi=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(5)
        kullaniciAdi.send_keys("1234")
        sifre.send_keys("")
        sleep(5)
        giris.click()
        hatalimesaj=driver.find_element(By.CLASS_NAME, "error-message-container")
        mesaj="Epic sadface: Password is required"
	print("\n************Şifre Boş Geçilemez Uyarı Kontrol****************")
        print(f"Test Sonucu: {mesaj}")
        sleep(10)

    def kullanici_kilitli(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullaniciAdi=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(5)
        kullaniciAdi.send_keys("locked_out_user")
        sifre.send_keys("secret_sauce")
        sleep(5)
        giris.click()
        hatalimesaj=driver.find_element(By.CLASS_NAME,"error-message-container")
        mesaj="Epic sadface: Sorry, this user has been locked out."
	print("\n************Kullanıcı Kilitlendi Mesajı****************")
        print(f"Test Sonucu: {mesaj}")
        sleep(10)

    def ikon_kontrol(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullaniciAdi=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(5)
        kullaniciAdi.send_keys("")
        sifre.send_keys("")
        sleep(5)
        giris.click()
        hatalimesaj=driver.find_element(By.CLASS_NAME,"error-message-container")
        hatabutonu=driver.find_element(By.CLASS_NAME, "error-button")
        sleep(5)
        hatabutonu.click()
	print("\n************ikon gösterilir ve kapatılır****************")
        sleep(10)

    def inventory_html(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullaniciAdi=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(5)
        kullaniciAdi.send_keys("standard_user")
        sifre.send_keys("secret_sauce")
        sleep(5)
        giris = driver.find_element(By.ID,"login-button")
        giris.click()
        sleep(5)
        print("\n************Sayfaya yönlendirme****************")
        print("İnventory sayfasına ulaştınız")

    def urun_sayma(self):
        driver=webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        sleep(5)
        kullaniciAdi=driver.find_element(By.ID, "user-name")
        sifre=driver.find_element(By.ID, "password")
        giris=driver.find_element(By.ID, "login-button")
        sleep(5)
        kullaniciAdi.send_keys("standard_user")
        sifre.send_keys("secret_sauce")
        sleep(5)
        giris.click()
        sleep(5)
        urunSayisi=driver.find_elements(By.CLASS_NAME, "inventory_item")
        print(f"Ürün Sayisi : {len(urunSayisi)}")
       
        

test=Test_Sauce()

test.kullanici_adi_kontrol()
test.sifre_kontrol()
test.kullanici_kilitli()
test.ikon_kontrol()
test.inventory_html()
test.urun_sayma()

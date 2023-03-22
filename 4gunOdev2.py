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

    def gorev_1(self):
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
        print(f"{mesaj}")
        sleep(10)

    def gorev_2(self):
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
        print(f"{mesaj}")
        sleep(10)

    def gorev_3(self):
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
        print(f"{mesaj}")
        sleep(10)

    def gorev_4(self):
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
        sleep(10)

    def gorev_5(self):
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
        current_URL="https://www.saucedemo.com/inventory.html"
        sleep(10)
        print(f"Current URL : {current_URL}")


    def gorev_6(self):
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

test.gorev_1()
test.gorev_2()
test.gorev_3()
test.gorev_4()
test.gorev_5()
test.gorev_6()

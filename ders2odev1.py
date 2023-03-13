# Bir öğrenci kayıt sistemi yazdığımızı düşünelim. Sistemimizdeki öğrencileri bir listede sadece ad soyad olacak şekilde tutalım.

# Bu öğrenci kayıt sistemine;

# Aldığı isim soy isim ile listeye öğrenci ekleyen
# Aldığı isim soy isim ile eşleşen değeri listeden kaldıran
# Listeye birden fazla öğrenci eklemeyi mümkün kılan
# Listedeki tüm öğrencileri tek tek ekrana yazdıran
# Öğrencinin listedeki index numarası öğrenci numarası olarak kabul edildiğini düşünerek öğrencinin numarasını öğrenmeyi mümkün kılan
# Listeden birden fazla öğrenci silmeyi mümkün kılan (döngü kullanınız)
# fonksiyonları geliştiriniz ve her bir fonksiyonu en az bir kere çağırarak konsolda test ediniz.

# Ödevde kullanacağınız döngülerin bir tanesi for bir tanesi while döngüsü olması istenmektedir

ogrenciler = []
#ogrenci eklemek için komut
def ogrenciEkle(count):
    for i in range(count):
        ad=input("Lütfen eklemek istediğiniz öğrenci adını giriniz: ")
        soyad=input("Lütfen eklemek istediğiniz öğrenci soyadını giriniz: ")
        adsoyad=ad+soyad
        ogrenciler.append(adsoyad)
        print("Öğrenci başarıyla kayıt edildi.")
        anaMenu()

#Öğrenci silmek için komut
def ogrenciSil(count):
    for i in range(count):
        ad=input("Lütfen silmek isteğiniz öğrencinin adını giriniz: ")
        soyad=input("Lütfen silmek istediğiniz öğrencinin soyadını giriniz: ")
        adsoyad=ad+soyad
        ogrenciler.remove(adsoyad)
        print("Öğrenci başarıyla silindi.")
        anaMenu()


#Çoklu öğrenci ekleme
def cokluOgrenciEkle():
    count=int(input("Kaç adet öğrenci eklemek istediğinizi giriniz: "))
    
    for i in range(count):
        ogrenciEkle(count)
    anaMenu()

#Çoklu öğrenci silme
def cokluOgrenciSil():
    count=int(input("Kaç adet öğrenci silmek istediğinizi giriniz: "))
    
    for i in range(count):
        ogrenciSil(count)
    anaMenu()


#Öğrenci listesini ekrana yazdırmak için
def ogrenciListele():
    print("Öğrenci listesi: ")
    for ad, soyad in ogrenciler:
        print(f"{ad},{soyad}")
    anaMenu()

#Programdan çıkış

def cikis():
    print("Programdan çıkılıyor.")
    exit()

#Kullanıcıya yapmak istediği işlemleri gösteriyoruz.

def anaMenu():
    islem = input("1- Öğrenci Ekle\n2- Öğrenci Sil\n3- Öğrencileri Listele\n4- Çoklu Öprenci Ekle\n5- Çoklu Öğrenci Sil\n6- Çıkış\nLütfen yapmak istediğiniz işlemi giriniz:")
    if islem == "1":
        ogrenciEkle(1)
    elif islem == "2":
        ogrenciSil(1)
    elif islem == "3":
        ogrenciListele()
    elif islem == "4":
        cokluOgrenciEkle()
    elif islem == "5":
        cokluOgrenciSil()
    elif islem == "6":
        cikis()
    else :
        print("Hatalı bir giriş yaptınız.\nLütfen tekrar deneyin.")
        anaMenu()
    
 
print("*****Öğrenci Kayıt Sistemine Hoşgeldiniz*****")
anaMenu()
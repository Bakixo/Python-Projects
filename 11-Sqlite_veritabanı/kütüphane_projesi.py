from Kütüphane import *

print("""******************************

Kütüphane Programına Hoşgeldiniz.

İşlemler;

1. Kitapları Göster

2. Kitap Sorgulama

3. Kitap Ekle

4. Kitap Sil

5. Baskı Yükselt
      
      
Çıkmak iin 'q' ya basın.     
      
******************************""")

while True:
    işlem = input("İşleminiz :")
    kütüphane = Kütüphane()
    
    if (işlem == "q"):
        print("Program sonlandırılıyor...")
        break
    elif (işlem == "1"):
        kütüphane.kitapları_göster()
    elif (işlem == "2"):
        isim = input("Hangi kitabı istiyosunuz ? :")
        print("Kitap sorgulanıyor...")
        time.sleep(2)
        kütüphane.kitap_sorgula(isim)
        
    elif (işlem == "3"):
        isim = input("Eklemek istediğiniz kitabın ismi:")
        yazar = input("Eklemek istediğiniz kitabın yazarı:")
        yayınevi = input("Eklemek istediğiniz kitabın yayinevi:")
        tür = input("Eklemek istediğiniz kitabın türü:")
        baskı = input("Eklemek istediğiniz kitabın baskısı:")
        
        yeni_kitap = Kitap(isim,yazar,yayınevi,tür,baskı)
        print("Kitap ekleniyor...")
        time.sleep(2)
        
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitabınız eklendi...")
        
    elif (işlem == "4"):
        isim = input("Hangi kitabı silmek istiyorsunuz ? ")
    
        cevap = input("Emin misiniz ? (E/H)")
        if (cevap == "E"):
            print("Kitap siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi...")
    elif (işlem == "5"):
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz ? :")
        print("Lütfen bekleyiniz...")
        time.sleep(2)
        kütüphane.baskı_yükselt(isim)
        print("Baskı yükseltildi....")
    else:
        print("Geçersiz işlem...")
            


import random
import time

class Kumanda():
    
    def __init__(self, tv_durum = "Kapali", tv_ses = 0, kanal_listesi = ["Trt"], kanal = "Trt"):
        
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        
    def tv_ac(self):
        
        if (self.tv_durum == "Açik"):
            print("Televizyonunuz zaten açik...")
        else:
            print("Televizyonunuz açiliyor...")
            self.tv_durum = "Açik"
    def tv_kapat(self):
        
        if (self.tv_durum == "Kapali"):
            print("Televizyon zaten kapali...")
        else:
            print("Televizyonunuz kapaniyor...")
            self.tv_durum = "Kapali"
            
    def ses_ayarları(self):
        
        while True:
            cevap = input("Sesi azalt: '<' \nSesi arttir: '>' \nÇikiş: çikiş")
            
            if(cevap == "<"):
                self.tv_ses -= 1
                print("Ses: ", self.tv_ses)
            elif(cevap == ">"):
                if(self.tv_ses != 32):
                    self.tv_ses += 1
                    print("Ses: ", self.tv_ses)
            else:
                print("Ses Güncellendi:", self.tv_ses)
                break
    def kanal_ekle(self,kanal_ismi):
        print("Kanal eklenyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi...")
    def rastgele_kanal(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Şu anki Kanal:",self.kanal)
    def __len__(self):
        return len(self.kanal_listesi)
    def __str__(self):
        return "Tv durumu: {}\nTv ses: {}\nKanal listesi: {}\n Şu anki kanal: {}\n".format(self.tv_durum, self.tv_ses, self.kanal_listesi, self.kanal)
            

kumanda = Kumanda()

print("""
      
Televizyon Uygulamasi 

1- Tv aç 
2- Tv kapat
3- Tv ses ayari
4- Kanal ekle
5- Kanal sayisini öğrenme
6- Rastgele kanala geçme
7- Televizyon bilgileri

Çikmak için 'q' ya basiniz.

      
""")


while True:
    işlem = input("işlemi Seçiniz:")
    
    if (işlem == "q"):
        print("Program sonlandırılıyor...")
        break
    
    elif (işlem == "1"):
        kumanda.tv_ac()
    elif (işlem == "2"):
        kumanda.tv_kapat()
    elif (işlem == "3"):
        kumanda.ses_ayarları()
    elif (işlem == "4"):
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak giriniz:")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)
    elif (işlem == "5"):
        print("Kanal sayısı:", len(kumanda))
    elif (işlem == "6"):
        kumanda.rastgele_kanal()
    elif (işlem == "7"):
        print(kumanda)
    else:
        print("Geçersiz işlem...")

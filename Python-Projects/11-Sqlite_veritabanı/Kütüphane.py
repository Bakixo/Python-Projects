import sqlite3
import time

class Kitap():
    
    def __init__(self,isim,yazar,yayinevi,tür,baski):
        
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tür = tür
        self.baski = baski
        
    def __str__(self):
        
        return "Kitap ismi: {}\nYazar: {}\nYayinevi: {}\nTür: {}\nBaskı: {}".format(self.isim,self.yazar,self.yayinevi,self.tür,self.baski)

class Kütüphane():
    
    def __init__(self):
        
        self.baglantı_olustur()
    def baglantı_olustur(self):
        self.baglantı = sqlite3.connect("kütüphane.db")
        
        self.cursor = self.baglantı.cursor()
        
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT, yazar TEXT, yayinevi TEXT, tür TEXT, baski INT)"
        
        self.cursor.execute(sorgu)
        
        self.baglantı.commit()
    
    def baglantiyi_kes(self):
        self.baglantı.close()
    def kitapları_göster(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        
        kitaplar = self.cursor.fetchall()
        
        if len(kitaplar) == 0:
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    def kitap_sorgula(self,isim):
        
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        
        self.cursor.execute(sorgu,(isim,))
        
        kitaplar = self.cursor.fetchall()
        
        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmuyor...")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
        
    def kitap_ekle(self,kitap):
        sorgu = "INSERT INTO kitaplar VALUES(?,?,?,?,?)"
        
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tür,kitap.baski))

        self.baglantı.commit()
    def kitap_sil(self,isim):
        
        sorgu = "DELETE FROM kitaplar WHERE isim = ?"
        
        self.cursor.execute(sorgu,(isim,))
        
        self.baglantı.commit()
    
    def baskı_yükselt(self,isim):
        
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        
        self.cursor.execute(sorgu,(isim,))
        
        kitaplar =  self.cursor.fetchall()
        
        if(len(kitaplar) == 0):
            print("Böyle bir kitap bulunmuyor...")
        else:
            baski = kitaplar[0][4]
            baski += 1
            
            sorgu2 = "UPDATE kitaplar SET baski = ? WHERE isim = ?"
            
            self.cursor.execute(sorgu2,(baski,isim))
            
            self.baglantı.commit()
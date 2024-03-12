import sys
from PyQt5 import QtCore, QtWidgets, QtGui
import sqlite3

class Pencere(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()

        self.baglanti_olustur()

        self.init_ui()

    def init_ui(self):
        
        self.buton = QtWidgets.QPushButton("Giriş Yap")
        self.kullanici_adi = QtWidgets.QLineEdit()
        self.sifre = QtWidgets.QLineEdit()
        self.sifre.setEchoMode(QtWidgets.QLineEdit.Password)
        self.yazi_alani = QtWidgets.QLabel("")
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.kullanici_adi)
        h_box.addWidget(self.sifre)
        h_box.addStretch()
 
        v_box = QtWidgets.QVBoxLayout()
        v_box.addLayout(h_box)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.buton)
        
        self.setLayout(v_box)
        self.setWindowTitle("Kullanıcı girişi")
        self.setGeometry(700, 300, 300, 300)
        self.yazi_alani.setGeometry(300,300,400,400)
        
        self.buton.clicked.connect(self.login)
        
        self.buton_ekle = QtWidgets.QPushButton("Kayıt ol")
        self.buton_ekle.clicked.connect(self.yeni_kullanici_ekle)
        v_box.addWidget(self.buton_ekle)
        
        self.show()
        
    def baglanti_olustur(self):
        
        self.baglanti = sqlite3.connect("Kullanici_girisi.db")
        print(self.baglanti)
        self.cursor = self.baglanti.cursor()
    
        self.cursor.execute("CREATE TABLE IF NOT EXISTS kullanicilar (kullanici_adi TEXT, parola TEXT)")  
        self.baglanti.commit()
    
    def login(self):
        adi = self.kullanici_adi.text()
        par = self.sifre.text()

        self.cursor.execute("SELECT * FROM kullanicilar WHERE kullanici_adi = ?", (adi,))
        data = self.cursor.fetchone()
        veritabani_sifre = data[1] if data else None
    
        if veritabani_sifre is not None and veritabani_sifre == par:
            self.yazi_alani.setText(f"Hoşgeldiniz {adi}!")
        else:
            self.yazi_alani.setText("Kullanıcı adı veya şifre hatalı!")

    
    def yeni_kullanici_ekle(self):
        adi = self.kullanici_adi.text()
        par = self.sifre.text()
    
        if adi and par:
            self.kullanici_ekle(adi,par)
            self.yazi_alani.setText("Yeni kullanıcı eklendi: " + adi)
        else:
            self.yazi_alani.setText("Kullanıcı adı ve parola alanlarını doldurun!")

    def kullanici_ekle(self, kullanici_adi, parola):
        self.cursor.execute("INSERT INTO kullanicilar (kullanici_adi, parola) VALUES (?, ?)", (kullanici_adi, parola))
        self.baglanti.commit()
    
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())

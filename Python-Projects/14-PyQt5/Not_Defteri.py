import sys
from PyQt5 import QtWidgets, QtGui
import os
from PyQt5.QtWidgets import QAction,qApp,QMainWindow

class Pencere(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.init_ui()
        
    def init_ui(self):
        self.yazi_alani = QtWidgets.QTextEdit()
        self.temizle_butonu = QtWidgets.QPushButton("Temizle")
        self.ac_butonu = QtWidgets.QPushButton("Aç")
        self.kaydet_butonu = QtWidgets.QPushButton("Kaydet")
        
        h_box = QtWidgets.QHBoxLayout()
        h_box.addWidget(self.temizle_butonu)
        h_box.addWidget(self.ac_butonu)
        h_box.addWidget(self.kaydet_butonu)
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)
        
        self.setLayout(v_box)
        self.setGeometry(800,300,500,500)
        
        self.temizle_butonu.clicked.connect(self.Temizle)
        self.ac_butonu.clicked.connect(self.dosya_ac)
        self.kaydet_butonu.clicked.connect(self.dosya_kaydet)
        
    def Temizle(self):
        self.yazi_alani.clear()
    
    def dosya_ac(self):
        dosya_ismi = QtWidgets.QFileDialog.getOpenFileName(self,"Dosya Aç",os.getenv("HOME"))
        if dosya_ismi[0]:
            with open(dosya_ismi[0],"r") as file:
                self.yazi_alani.setText(file.read())
    def dosya_kaydet(self):
        dosya_ismi = QtWidgets.QFileDialog.getSaveFileName(self,"Dosya Kaydet",os.getenv("HOME"))
        if dosya_ismi[0]:
            with open(dosya_ismi[0],"w") as file:

                file.write(self.yazi_alani.toPlainText())
            
class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.pencere = Pencere()
        self.setCentralWidget(self.pencere)
        
        self.menuleri_olustur()

    def menuleri_olustur(self):
        menubar = self.menuBar()
        
        dosya = menubar.addMenu("Dosya")
        dosya_ac = QAction("Dosya Aç",self)
        dosya_ac.setShortcut("CTRL+O")
        
        dosya_kaydet = QAction("Dosya Kaydet",self)
        dosya_kaydet.setShortcut("CTRL+S")
        
        temizle = QAction("Dosyayı Temizle",self)
        temizle.setShortcut("CTRL+D")
        
        cikis = QAction("Çıkış",self)
        cikis.setShortcut("CTRL+Q")
                
        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(temizle)
        dosya.addAction(cikis)
        
        dosya.triggered.connect(self.response)
        
        self.setWindowTitle("Not Arayüzü")
        self.show()
    def response(self,action):
        
        if action.text() == "Dosya Aç":
            self.pencere.dosya_ac()
        elif action.text() == "Dosya Kaydet":
            self.pencere.dosya_kaydet()
        elif action.text() == "Dosyayı Temizle":
            self.pencere.Temizle()
        elif action.text() == "Çıkış":
            qApp.quit()
            
app = QtWidgets.QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())
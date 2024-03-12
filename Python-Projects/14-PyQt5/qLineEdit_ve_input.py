import sys 
from PyQt5 import QtWidgets , QtGui

class Pencere(QtWidgets.QWidget):
    
    def __init__(self):
        
        super().__init__()
        
        self.init_ui()
    
    def init_ui(self):
        
        self.yazi_alani = QtWidgets.QLineEdit()
        self.temizle = QtWidgets.QPushButton("Temizle")
        self.yazdir = QtWidgets.QPushButton("Yazdir")
        self.sonuç_etiketi = QtWidgets.QLabel("")
        
        v_box = QtWidgets.QVBoxLayout()
        
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.temizle)
        v_box.addWidget(self.yazdir)
        v_box.addStretch()
        v_box.addWidget(self.sonuç_etiketi)
        v_box.addStretch()
        
        h_box = QtWidgets.QHBoxLayout()
        
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        
        
        self.setGeometry(700,300,300,300)
        self.setLayout(h_box)
        
        
        self.temizle.clicked.connect(self.Temizle)
        self.yazdir.clicked.connect(self.Yazdir)
        self.show()
    
    def Temizle(self):
        self.yazi_alani.clear()
        self.sonuç_etiketi.setText("")
        
    def Yazdir(self):
        metin = self.yazi_alani.text()
        self.sonuç_etiketi.setText(metin)
        
        
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
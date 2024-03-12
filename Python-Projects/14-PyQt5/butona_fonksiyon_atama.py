import sys
import typing 
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QWidget

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()

        self.init_ui()
    def init_ui(self):
        
        self.yazi_alani= QtWidgets.QLabel("Bana henüz tiklanmadi")
        self.buton = QtWidgets.QPushButton("Bana tikla")
        self.say = 0
        
        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.buton)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()

        self.setLayout(h_box)
        
        self.buton.clicked.connect(self.click)
        self.show() 

    def click(self):
        self.say += 1
        self.yazi_alani.setText("Bana " + str(self.say) + " defa tiklandi")
        
app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
pencere.setGeometry(700,300,300,300)

sys.exit(app.exec_())
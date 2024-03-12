import sys
import typing 
from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QWidget,QLabel

class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):
        
        self.checkbox = QtWidgets.QCheckBox("Pythonu seviyor musunuz ?")
        self.yazi_alani = QLabel("")
        self.buton = QtWidgets.QPushButton("Gönder")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.checkbox)
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)

        self.setLayout(v_box)
        
        self.setWindowTitle("CHECKBOX")
        
        self.buton.clicked.connect(lambda : self.click(self.checkbox.isChecked(),self.yazi_alani))
        self.setGeometry(700,400,200,200)
        self.show()
        
    def click(self,checkbox,yazi_alani):
        if checkbox:
            yazi_alani.setText("harika!")
        else:
            yazi_alani.setText("neden ?!")



app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
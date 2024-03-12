import sys
from PyQt5 import QtCore, QtWidgets,QtGui


class Pencere(QtWidgets.QWidget):

    def __init__(self):

        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.radio_yazisi = QtWidgets.QLabel("hangi dili daha çok seviyorsunuz ? ")
        self.java = QtWidgets.QRadioButton("JAVA")
        self.python = QtWidgets.QRadioButton("PYTHON")
        self.c = QtWidgets.QRadioButton("C")

        self.yazi_alani = QtWidgets.QLabel("")
        self.buton = QtWidgets.QPushButton("GÖNDER")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.c)
        v_box.addWidget(self.python)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.buton)
        v_box.addStretch()

        self.setLayout(v_box)
        self.buton.clicked.connect(lambda : self.click(self.c.isChecked(),self.java.isChecked(),self.python.isChecked(),self.yazi_alani))
        self.setWindowTitle("Radio button")
        self.show()
    def click(self,c,java,python,yazi_alani):
        if c:
            yazi_alani.setText("C !?")
        if java:
            yazi_alani.setText("JAVA!")
        if python:
            yazi_alani.setText("PYTHON!")

app = QtWidgets.QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
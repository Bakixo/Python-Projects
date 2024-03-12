import sys 
from PyQt5 import QtWidgets,QtGui

def pencere():

    app= QtWidgets.QApplication(sys.argv)

    buton= QtWidgets.QPushButton("TAMAM")
    buton2 = QtWidgets.QPushButton("İPTAL")

    h_box = QtWidgets.QHBoxLayout()
    h_box.addWidget(buton)
    h_box.addWidget(buton2)
    h_box.addStretch()

    v_box = QtWidgets.QVBoxLayout()
    v_box.addStretch()
    v_box.addLayout(h_box)


    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("PYTHON")
    pencere.setGeometry(700,300,500,500)

    pencere.setLayout(v_box)
    pencere.show()

    sys.exit(app.exec_())
pencere()
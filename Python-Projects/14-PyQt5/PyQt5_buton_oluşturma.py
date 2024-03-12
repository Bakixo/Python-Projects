import sys  
from PyQt5 import QtWidgets,QtGui

def pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Buton Oluşturma")
    pencere.setGeometry(700,300,500,500)

    buton = QtWidgets.QPushButton(pencere)
    buton.setText("Buton")
    buton.move(200,200)
    buton = QtWidgets.QLabel(pencere)


    pencere.show()
    sys.exit(app.exec_())

pencere()
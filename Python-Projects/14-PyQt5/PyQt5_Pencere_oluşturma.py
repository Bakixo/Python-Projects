import sys
from PyQt5 import QtWidgets,QtGui

def pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Pencere")
    pencere.setGeometry(700,300,500,500)

    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("DENEME YAZISI")
    etiket1.move(200,200)

    pencere.show()

    sys.exit(app.exec_())
    
pencere()
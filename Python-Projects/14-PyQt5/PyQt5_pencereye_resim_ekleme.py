import sys
from PyQt5 import QtWidgets,QtGui

def pencere():

    app = QtWidgets.QApplication(sys.argv)

    pencere = QtWidgets.QWidget()
    pencere.setWindowTitle("Pencere")
    pencere.setGeometry(700,300,500,500)

    etiket1 = QtWidgets.QLabel(pencere)
    etiket1.setText("DENEME YAZISI")
    etiket1.move(100,200)

    etiket2 = QtWidgets.QLabel(pencere)
    etiket2.setPixmap(QtGui.QPixmap("resim.png"))
    etiket2.move(200,200)

    pencere.show()

    sys.exit(app.exec_())
    
pencere()
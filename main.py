import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget

#Cargar formulario *.ui
form_class = uic.loadUiType("diseno.ui")[0]

#crear clase MyWindowClass
class MyWindowClass(QWidget, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pantallas.setCurrentIndex(1)# activamos la pantalla 1



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()






import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget

from Clase_Serie import *
from Classe_Pelicula import *

#include "comboboxdialog.h"
#include "ui_comboboxdialog.h"

# Cargar formulario *.ui
form_class = uic.loadUiType("diseno.ui")[0]


# crear clase MyWindowClass
class MyWindowClass(QMainWindow, form_class):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pantallas.setCurrentIndex(0)  # activamos la pantalla 1

    def btpulsado(self):
        self.pantallas.setCurrentIndex(1)
        nombre = self.sender().objectName()
        pelicula1 = Pelicula(nombre)
        titulo_pelicula = str(pelicula1.getTitulo())
        genero_pelicula = pelicula1.getGenero()
        duracion_pelicula = str(pelicula1.getDuracion())
        visto_pelicula = pelicula1.getVisto()
        self.titulo.setText(titulo_pelicula)
        self.genero.setText(genero_pelicula)
        self.duracion.setText(duracion_pelicula)
        self.visto.setText(visto_pelicula)

    def btserie(self):
        self.pantallas.setCurrentIndex(2)
        nombre = self.sender().objectName()
        serie1 = Serie(nombre)
        titulo_serie = serie1.getTitulo()
        self.titulo_2.setText(titulo_serie)



    def volver(self):
        self.pantallas.setCurrentIndex(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()


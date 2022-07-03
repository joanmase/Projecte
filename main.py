import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QMessageBox
import pandas as pd
import openpyxl

from Clase_Serie import *
from Classe_Pelicula import *
from Clase_Temporada import *
from Clase_Capitulo import *
from Usuario import *

with pd.ExcelFile("Pelis.xlsx") as xls:
    Peliculas = pd.read_excel(xls, "Peliculas")
    Peliculas_dicc = Peliculas.to_dict()

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
        self.pantallas.setCurrentIndex(2)
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
        self.pantallas.setCurrentIndex(3)
        nombre = self.sender().objectName()
        serie1 = Serie(nombre)
        titulo_serie = serie1.getTitulo()
        self.tituloserie.setText(titulo_serie)
        genero_serie = serie1.getGenero()
        self.genero_2.setText(genero_serie)
        self.suprimirTemporadas()
        self.listaTemporadas(serie1)
        self.suprimirCapitulos()
        self.listaCapitulos()
        self.getDuracionVistoCapitulo()

    def getDuracionVistoCapitulo(self):
        titulo_serie = self.tituloserie.text()
        temporada_actual = (self.temporada.currentIndex() + 1)
        titulo_capitulo = str(self.capitulo.currentText())
        clase = Capitulo(titulo_serie, temporada_actual, titulo_capitulo)
        duracion = str(clase.getDuracion())
        visto = str(clase.getVisto())
        self.duracion_3.setText(duracion)
        self.visto_2.setText(visto)


    def listaCapitulos(self):
        self.suprimirCapitulos()
        titulo_serie = self.tituloserie.text()
        temporada_actual = (self.temporada.currentIndex()+1)
        capitulos1 = Temporada(titulo_serie, temporada_actual)
        lista_capitulos = capitulos1.getCapitulos()
        self.capitulo.addItems(lista_capitulos)

    def listaTemporadas(self, serie):
        num_temporadas = serie.getTemporadas()
        x = []
        max = num_temporadas + 1
        for num in range(1, max):
            x.append('Temporada ' + str(num))
        self.temporada.addItems(x)


    def suprimirTemporadas(self):
        if self.temporada.itemText(1) != '':
            self.temporada.clear()
        else:
            self.temporada = self.temporada

    def suprimirCapitulos(self):
        if self.capitulo.itemText(1) != '':
            self.capitulo.clear()
        else:
            self.capitulo = self.capitulo

    def volver(self):
        self.pantallas.setCurrentIndex(1)

    def cerrar_sesion(self):
        pregunta2 = QMessageBox()
        pregunta2.setWindowTitle('Cerrar sesión')
        pregunta2.setText('Seguro que quieres cerrar sesión?')
        pregunta2.setIcon(QMessageBox.Question)
        pregunta2.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        resultado2 = pregunta2.exec_()
        if (resultado2 == 16384):
            self.pantallas.setCurrentIndex(0)
            self.lineEdit.clear()
            self.lineEdit_2.clear()
        else:
            self.pantallas.setCurrentIndex(1)


    def bt_iniciarsesion(self):
        nickname = self.lineEdit.text()
        contrasena = self.lineEdit_2.text()
        Usuario1 = Usuario(nickname, contrasena)
        if Usuario1.Iniciar_Sesion() == True:
            if Usuario1.Es_Admin() == False:
                self.pantallas.setCurrentIndex(1)
                self.label_2.setText('')
            else:
                self.pantallas.setCurrentIndex(4)
                self.label_2.setText('')
        else:
            self.label_2.setText('Usuario incorrecto')
            self.lineEdit.clear()
            self.lineEdit_2.clear()

    def bt_crearsesion(self):
        nickname = self.lineEdit.text()
        contrasena = self.lineEdit_2.text()
        Usuario1 = Usuario(nickname, contrasena)
        if Usuario1.Comprobar_User() == True:
            pregunta = QMessageBox()
            pregunta.setWindowTitle('Crear Usuario')
            pregunta.setText('Seguro que quieres crear el usuario?')
            pregunta.setIcon(QMessageBox.Question)
            pregunta.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            resultado = pregunta.exec_()
            print(resultado)
            if (resultado == 16384):
                Usuario1.Crear_Sesion()
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.label_2.setText('Usuario creado')

            else:
                self.lineEdit.clear()
                self.lineEdit_2.clear()
                self.label_2.setText('Usuario no creado')
        else:
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.label_2.setText('Usuario existente')

    def volver_2(self):
        self.pantallas.setCurrentIndex(4)

    def Insertar_Pelicula(self):
        self.pantallas.setCurrentIndex(5)

    def CrearPelicula(self):
        titulo = self.titulopelicula.text()
        duracion = self.duracionpelicula.text()
        genero = self.generopelicula.text()
        Pelicula1 = Pelicula(titulo)
        if titulo == '' or duracion == '' or genero == '':
            error2 = QMessageBox()
            error2.setWindowTitle('Error')
            error2.setText('Faltan campos por rellenar.')
            error2.setIcon(QMessageBox.Critical)
            error2.exec()
        elif Pelicula1.esPelicula()==True:
            error = QMessageBox()
            error.setWindowTitle('Error')
            error.setText('La película ya se encuentra en la plataforma.')
            error.setIcon(QMessageBox.Critical)
            error.exec()
        else:
            Pelicula1.Crear_Pelicula(titulo,duracion,genero)
            info = QMessageBox()
            info.setWindowTitle('Pelicula añadida')
            info.setText('La película ha sido añadida.')
            info.setIcon(QMessageBox.Information)
            self.titulopelicula.clear()
            self.duracionpelicula.clear()
            self.generopelicula.clear()
            info.exec()



    def compartir(self):
        nickname = self.lineEdit.text()
        contrasena = self.lineEdit_2.text()
        Usuario1 = Usuario(nickname, contrasena)
        pelicula = Peliculas_dicc.get('Fotografia')
        titulo = Peliculas_dicc.get('Titulo')
        serie = Capitulos_dicc.get('Fotografia')
        titulo2 = Capitulos_dicc.get('Serie')
        for i in titulo.keys():
            if str(titulo.get(i)) == str(self.titulo.text()):
                nombre = str(pelicula.get(i))

        for i in titulo2.keys():
            if titulo2.get(i) == self.tituloserie.text():
                nombre = serie.get(i)
        print(nombre)
        info = QMessageBox()
        info.setWindowTitle('Connexión')
        info.setText('Conectado/a correctamente')
        info.setIcon(QMessageBox.Information)
        Usuario1.servidor(nombre)
        info.exec()


    def connectar(self):
       nickname = self.lineEdit.text()
       contrasena = self.lineEdit_2.text()
       Usuario1 = Usuario(nickname, contrasena)
       info2 = QMessageBox()
       info2.setWindowTitle('Connectar')
       info2.setText('Conectado/a correctamente')
       info2.setIcon(QMessageBox.Information)
       msg = Usuario1.client()
       info2.exec()
       print(msg)
       pelicula1 = Pelicula(msg)
       serie1 = Serie(msg)
       if pelicula1.esPelicula()==True:
           titulo_pelicula = str(pelicula1.getTitulo())
           genero_pelicula = pelicula1.getGenero()
           duracion_pelicula = str(pelicula1.getDuracion())
           visto_pelicula = pelicula1.getVisto()
           self.titulo.setText(titulo_pelicula)
           self.genero.setText(genero_pelicula)
           self.duracion.setText(duracion_pelicula)
           self.visto.setText(visto_pelicula)
           self.pantallas.setCurrentIndex(2)
       elif serie1.esSerie()==True:
           titulo_serie = serie1.getTitulo()
           self.tituloserie.setText(titulo_serie)
           genero_serie = serie1.getGenero()
           self.genero_2.setText(genero_serie)
           self.suprimirTemporadas()
           self.listaTemporadas(serie1)
           self.suprimirCapitulos()
           self.listaCapitulos()
           self.getDuracionVistoCapitulo()
           self.pantallas.setCurrentIndex(3)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    MyWindow = MyWindowClass(None)
    MyWindow.show()
    app.exec_()


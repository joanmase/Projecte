import pandas as pd
import openpyxl
with pd.ExcelFile("Series.xlsx") as xls:
    Capitulos = pd.read_excel(xls, "Capitulo")
    Capitulos_dicc = Capitulos.to_dict()

from Clase_Serie import *
from Clase_Temporada import *

class Capitulo:
    def __init__(self, serie, temporada, titulo):
        """

        :param imagen: imagen de la serie
        """
        self.serie = serie
        self.temporada = temporada
        self.titulo = titulo

    def getDuracion(self):
        serie = Capitulos_dicc.get('Serie')
        temporadas = Capitulos_dicc.get('Temporada')
        capitulos = Capitulos_dicc.get('Titulo')
        duracion = Capitulos_dicc.get('Duracion')
        for i in serie.keys():
            if serie.get(i) == self.serie:
                if temporadas.get(i) == self.temporada:
                    if capitulos.get(i) == self.titulo:
                        return duracion.get(i)
        return False

    def getVisto(self):
        serie = Capitulos_dicc.get('Serie')
        temporadas = Capitulos_dicc.get('Temporada')
        capitulos = Capitulos_dicc.get('Titulo')
        visto = Capitulos_dicc.get('Visto')
        for i in serie.keys():
            if serie.get(i) == self.serie:
                if temporadas.get(i) == self.temporada:
                    if capitulos.get(i) == self.titulo:
                        return visto.get(i)
        return False


import pandas as pd
import openpyxl
with pd.ExcelFile("Pelis_series.xlsx") as xls:
    Capitulos = pd.read_excel(xls, "Capitulo")
    Capitulos_dicc = Capitulos.to_dict()

from Clase_Serie import *

class Temporada:
    def __init__(self, serie, temporada):
        """

        :param imagen: imagen de la serie
        """
        self.serie = serie
        self.temporada = temporada

    def getCapitulos(self):
        serie = Capitulos_dicc.get('Serie')
        temporadas = Capitulos_dicc.get('Temporada')
        capitulos = Capitulos_dicc.get('Titulo')
        todos_capitulos = []
        for i in serie.keys():
            if serie.get(i) == self.serie:
                if temporadas.get(i) == (self.temporada):
                    todos_capitulos.append(capitulos.get(i))
        return todos_capitulos


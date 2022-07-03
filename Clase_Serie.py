import pandas as pd
import openpyxl
with pd.ExcelFile("Series.xlsx") as xls:
    Capitulos = pd.read_excel(xls, "Capitulo")
    Capitulos_dicc = Capitulos.to_dict()

class Serie:
    """
    Clase para series
    """
    def __init__(self,imagen):
        """

        :param imagen: imagen de la serie
        """
        self.imagen = imagen

    def esSerie(self):
        serie = Capitulos_dicc.get('Fotografia')
        for i in serie.keys():
            if serie.get(i) == self.imagen:
                return True
        return False

    def getTitulo(self):
        serie = Capitulos_dicc.get('Fotografia')
        titulo = Capitulos_dicc.get('Serie')
        for i in serie.keys():
            if serie.get(i) == self.imagen:
                nombre_serie = titulo.get(i)
        return nombre_serie

    def getGenero(self):
        serie = Capitulos_dicc.get('Fotografia')
        genero = Capitulos_dicc.get('Genero')
        for i in serie.keys():
            if serie.get(i) == self.imagen:
                genero_serie = genero.get(i)
        return genero_serie

    def getTemporadas(self):
        serie = Capitulos_dicc.get('Fotografia')
        temporadas = Capitulos_dicc.get('Temporada')
        todas_temporadas = []
        for i in serie.keys():
            if serie.get(i) == self.imagen:
                todas_temporadas.append(temporadas.get(i))
        return max(todas_temporadas)





    



import pandas as pd
import openpyxl
with pd.ExcelFile("Pelis.xlsx") as xls:
    Peliculas = pd.read_excel(xls, "Peliculas")
    Peliculas_dicc = Peliculas.to_dict()

class Pelicula:
    """
    Clase para películas
    """
    def __init__(self, imagen):
        """

        :param imagen: imagen de la película
        """
        self.imagen=imagen

    def esPelicula(self):

        pelicula = Peliculas_dicc.get('Fotografia')
        for i in pelicula.keys():
            if pelicula.get(i) == self.imagen:
                return True
        return False

    def getTitulo(self):
        """

        :return: Para cada imagen, devuelve el título de la película
        """
        pelicula = Peliculas_dicc.get('Fotografia')
        titulo = Peliculas_dicc.get('Titulo')
        for i in pelicula.keys():
            if pelicula.get(i) == self.imagen:
                return titulo.get(i)
        return False

    def getGenero(self):
        """

        :return: Para cada imagen, devuelve el género de la película
        """
        pelicula = Peliculas_dicc.get('Fotografia')
        genero = Peliculas_dicc.get('Genero')
        for i in pelicula.keys():
            if pelicula.get(i) == self.imagen:
                return genero.get(i)
        return False

    def getDuracion(self):
        pelicula = Peliculas_dicc.get('Fotografia')
        duracion = Peliculas_dicc.get('Duracion')
        for i in pelicula.keys():
            if pelicula.get(i) == self.imagen:
                return duracion.get(i)
        return False

    def getVisto(self):
        pelicula = Peliculas_dicc.get('Fotografia')
        visto = Peliculas_dicc.get('Visto')
        for i in pelicula.keys():
            if pelicula.get(i) == self.imagen:
                return visto.get(i)
        return False

    '''def Crear_Pelicula(self, titulonuevo, generonuevo, duracionnueva):
        pelicula = Peliculas_dicc.get('Fotografia')
        titulo = Peliculas_dicc.get('Titulo')
        genero = Peliculas_dicc.get('Genero')
        duracion = Peliculas_dicc.get('Duracion')
        visto = Peliculas_dicc.get('Visto')
        for i in titulo.keys():
            if titulo.get(i) == '':
                titulo.get(i) == titulonuevo
                genero.get(i) == generonuevo
                duracion.get(i) == duracionnueva
    '''


    def Crear_Pelicula(self, titulonuevo, generonuevo, duracionnueva):
        '''
        '''
        pelicula = Peliculas_dicc.get('Fotografia')
        titulo = Peliculas_dicc.get('Titulo')
        genero = Peliculas_dicc.get('Genero')
        duracion = Peliculas_dicc.get('Duracion')
        visto = Peliculas_dicc.get('Visto')
        num_pelis = len(pelicula)
        pelicula[num_pelis] = titulonuevo
        titulo[num_pelis] = titulonuevo
        genero[num_pelis] = generonuevo
        duracion[num_pelis] = duracionnueva
        visto[num_pelis] = 'No'
        df2 = pd.DataFrame([[Peliculas_dicc['Fotografia'][key],Peliculas_dicc['Titulo'][key],
                             Peliculas_dicc['Genero'][key],Peliculas_dicc['Duracion'][key],
                             Peliculas_dicc['Visto'][key]]for key in Peliculas_dicc['Fotografia'].keys()],
                           columns = ['Fotografia', 'Titulo','Genero','Duracion','Visto'])
        df2.to_excel("Pelis.xlsx",
            sheet_name='Peliculas')
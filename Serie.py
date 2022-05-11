from Temporada import *

class Serie:
    """
    Clase para Series
    """

    def __init__(self, titulo, genero, lista_temporadas):
        """
        >>> Serie1 = Serie('Serie1','Drama', {'Temporada1': 1, 'Temporada2': 2})
        >>> Serie1.titulo
        'Serie1'
        >>> Serie1.genero
        'Drama'
        >>> Serie1.lista_temporadas
        {'Temporada1': 1, 'Temporada2': 2}

        """
        self.titulo= titulo
        self.genero = genero
        self.lista_temporadas = lista_temporadas

        def getTitulo(self):
            """
            >>> Serie1 = Serie('Serie1','Drama', {'Temporada1': 1, 'Temporada2': 2})
            >>> getTitulo(Serie1)
            'Serie1'

            :return: Devuelve el nombre de la pelicula
            """
            return self.titulo

        def getNum_Temporadas(self):
            """
            >>> Serie1 = Serie('Serie1','Drama', {'Temporada1': 1, 'Temporada2': 2})
            >>> getNum_Temporadas(Serie1)
            2

            :return: Devuelve la duracion de la pelicula
            """
            return len(self.lista_temporadas)

        def getGenero(self):
            """
            >>> Serie1 = Serie('Serie1','Drama', {'Temporada1': 1, 'Temporada2': 2})
            >>> getGenero(Serie1)
            {'Titulo1': 1, 'Titulo2': 2}

            :param self:
            :return:
            """
            return self.genero



if __name__ == '__main__':
    import doctest

    doctest.testmod()

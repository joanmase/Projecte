from Capitulo import *

class Temporada:
    """
    Clase para temporadas
    """

    def __init__(self, num_temporada, lista_capitulos):
        """
        >>> Temporada1 = Temporada(1, {'Titulo1': 1, 'Titulo2': 2})
        >>> Temporada1.num_temporada
        1
        >>> Temporada1.lista_capitulos
        {'Titulo1': 1, 'Titulo2': 2}

        :param num_temporada:
        :param lista_capitulos:
        """
        self.num_temporada= num_temporada
        self.lista_capitulos = lista_capitulos

        def getNum_Temporada(self):
            """
            >>> Temporada1 = Temporada(1, {'Titulo1': 1, 'Titulo2': 2})
            >>> getNum_Temporada(Temporada1)
            1

            :return: Devuelve el nombre de la pelicula
            """
            return self.num_temporada

        def getNum_capitulos(self):
            """
            >>> Temporada1 = Temporada(1, {'Titulo1': 1, 'Titulo2': 2})
            >>> getNum_capitulos(Temporada1)
            2

            :return: Devuelve la duracion de la pelicula
            """
            return len(self.lista_capitulos)

        def getLista_Capitulos(self):
            """
            >>> Temporada1 = Temporada(1, {'Titulo1': 1, 'Titulo2': 2})
            >>> getLista_Capitulos(Temporada1)
            {'Titulo1': 1, 'Titulo2': 2}

            :param self:
            :return:
            """
            return self.lista_capitulos



if __name__ == '__main__':
    import doctest

    doctest.testmod()

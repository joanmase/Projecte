class Capitulo:
    """
    Clase para películas
    """

    def __init__(self, titulo, num_capitulo, duracion,  visto):
        """
        >>> Principio = Capitulo('Principio', 1, 45, False)
        >>> Principio.titulo
        'Principio'
        >>> Principio.duracion
        45
        >>> Principio.num_capitulo
        1
        >>> Principio.visto
        False

        :param titulo: titulo del capítulo
        :param duracion: duración del capítulo
        :param num_capitulo: número del capítulo
        :param visto: si se ha visto dicho capítulo
        """
        self.titulo = titulo
        self.num_capitulo = num_capitulo
        self.duracion = duracion
        self.visto = False

        def getTitulo(self):
            """
            >>> Principio = Capitulo('Principio', 1, 45, False)
            >>> getTitulo(Principio)
            'Principio'

            :return: Devuelve el nombre de la pelicula
            """
            return self.titulo
        def getDuracion(self):
            """
            >>> Principio = Capitulo('Principio', 1, 45, False)
            >>> getDuracion(Principio)
            128

            :return: Devuelve la duracion de la pelicula
            """
            return self.duracion
        def getNumCapitulo(self):
            """
            >>> Principio = Capitulo('Principio', 1, 45, False)
            >>> getNumCapitulo(Principio)
            1

            :return: Devuelve la duracion de la pelicula
            """
            return self.num_capitulo
        def getVisto(self):
            """
            >>> Principio = Capitulo('Principio', 1, 45, False)
            >>> getVisto(Principio)
            False

            :return: Devuelve la duracion de la pelicula
            """
            return self.visto

        def DatosCapitulo(self):
            """
            >>> Principio = Capitulo('Principio', 1, 45, False)
            >>> DatosCapitulo(Principio)
            Titulo: Principio
            Duracion: 45
            Numero Capitulo: 1
            Visto: No

            :return: Devuelve los datos de la pelicula
            """
            x = self.visto
            if x == False:
                Visto = 'No'
            else:
                Visto = 'Si'
            print("\nTitulo:" +self.getTitulo()+"\nDuracion:" +str(self.getDuracion())+"\nNumero Capitulo:" +self.getNumCapitulo()+"\nVisto:" +Visto)



if __name__ == '__main__':
    import doctest

    doctest.testmod()

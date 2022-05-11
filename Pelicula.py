class Pelicula:
    """
    Clase para películas
    """

    def __init__(self, titulo, duracion, genero, visto):
        """
        >>> Titanic = Pelicula('Titanic', 128, 'Drama', False)
        >>> Titanic.titulo
        'Titanic'
        >>> Titanic.duracion
        128
        >>> Titanic.genero
        'Drama'
        >>> Titanic.visto
        False

        :param titulo: titulo de la película
        :param duracion: duración de la película
        :param genero: género de la película
        :param visto: si se ha visto dicha película
        """
        self.titulo = titulo
        self.duracion = duracion
        self.genero = genero
        self.visto = False

        def getTitulo(self):
            """
            >>> Titanic = Pelicula('Titanic', 128, 'Drama', False)
            >>> getTitulo(Titanic)
            'Titanic'

            :return: Devuelve el nombre de la pelicula
            """
            return self.titulo

        def getDuracion(self):
            """
            >>> Titanic = Pelicula('Titanic', 128, 'Drama', False)
            >>> getDuracion(Titanic)
            128

            :return: Devuelve la duracion de la pelicula
            """
            return self.duracion

        def getGenero(self):
            """
            >>> Titanic = Pelicula('Titanic', 128, 'Drama', False)
            >>> getGenero(Titanic)
            'Drama'

            :return: Devuelve la duracion de la pelicula
            """
            return self.genero

        def getVisto(self):
            """
            >>> Titanic = Pelicula('Titanic', 128, 'Drama', False)
            >>> getVisto(Titanic)
            False

            :return: Devuelve la duracion de la pelicula
            """
            return self.visto

        def DatosPelicula(self):
            """
            >>> Titanic = Pelicula('Titanic', 128, 'Drama', False)
            >>> DatosPelicula(Titanic)
            Titulo: Titanic
            Duracion: 128
            Genero: Drama
            Visto: No

            :return: Devuelve los datos de la pelicula
            """
            x = self.visto
            if x == False:
                Visto = 'No'
            else:
                Visto = 'Si'
            print("\nTitulo:" +self.getTitulo()+"\nDuracion:" +str(self.getDuracion())+"\nGenero:" +self.getGenero()+"\nVisto:" +Visto)

if __name__ == '__main__':
    import doctest

    doctest.testmod()

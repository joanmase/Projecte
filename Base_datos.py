import pandas as pd
'''
instal·lar pandas i openpyxl
'''

class Base_datos:

    def __init__(self, nombre_archivo,nombre_pag):
        """
        >>> Base_datos1 = Base_datos('Pelis_series.xlsx','Peliculas')
        >>> Base_datos1.nombre_archivo
        'Pelis_series.xlsx'

        :param num_temporada:
        :param lista_capitulos:
        """
        self.nombre_archivo = nombre_archivo
        self.nombre_pag = nombre_pag


    def leer_archivo(self):
        '''
        >>> Base_datos1 = Base_datos('Pelis_series.xlsx',sheet_name = 'Peliculas')
        >>> leer_archivo(Base_datos1)
        {'Numero': {0: 1, 1: 2}, 'Peliculas': {0: 'Iron Man', 1: 'Titanic'}}
        '''
        df = pd.read_excel(self.nombre_archivo,sheet_name=self.nombre_pag)
        new_dict = df.to_dict()

        return new_dict



if __name__ == '__main__':
    import doctest

    doctest.testmod()



'''
pd.read_excel(  on esta a l'ordinador, 
                sheet_name = 'nom de la fulla excel',
                usecols = ['primera columna que volem usar','...','...']
                )
Més a : https://pandas.pydata.org/docs/user_guide/io.html#excel-files
'''

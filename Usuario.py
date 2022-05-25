import pandas as pd

from Base_datos import*
class Usuario:
    """
    Clase para los usuarios
    """

    def __init__(self, datos):
        """
        >>> Usuario1 = Usuario({'usuario1': 'contrasena1'})
        >>> Usuario1.datos
        {'usuario1': 'contrasena1'}

        :param nick:
        :param contrasena:
        """
        self.datos = datos

    def Iniciar_Sesion(self,nick,contrasena):
        '''
        '''
        if contrasena == self.datos.get(nick):
            return True
        else:
            return False

    def Crear_Sesion(self,nick,contrasena):
        '''
        '''
        df=pd.DataFrame(nick,contrasena)
        Usuarios = Base_datos.leer_archivo(Base_datos('Pelis_series.xlsx',sheet_name = 'Usuarios'))
        num_usuarios = len(Usuarios)
        xlWriterDF = pd.ExcelWriter('Pelis_series.xlsx')
        for i in Usuarios.keys():
            if nick == i:
                return False
            else:
                Usuarios.to_excel(
                    excel_writer=xlWriterDF,
                    sheet_name='Usuarios',
                    na_rep='Missing',
                    columns=[nick,contrasena],
                    startcol= num_usuarios+1
                )
        return True




if __name__ == '__main__':
    import doctest

    doctest.testmod()
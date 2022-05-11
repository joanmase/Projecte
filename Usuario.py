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

   def Iniciar_Sesion(self):
        """
        >>> Usuario1 = Usuario({'usuario1': 'contrasena1'})
        >>> Iniciar_Sesion(Usuario1)
        :param self:
        :return:
        """
        print('Usuario:')
        nick = input()
        print = ('Contraseña:')
        contrasena = input()
        if contrasena == self.datos.get(nick):
            return print('Bienvenido'+nick)
        else:
            return print('Usuario incorrecto')



if __name__ == '__main__':
    import doctest

    doctest.testmod()
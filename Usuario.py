import pandas as pd
import socket

from Base_datos import*
class Usuario:
    """
    Clase para los usuarios
    """

    def __init__(self, nick, contrasena):
        """
        """

        self.nick = nick
        self.contrasena = contrasena

    def getdatos(self):
        """
        """
        return [self.nick,self.contrasena]

    def Iniciar_Sesion(self):
        '''
        '''
        Base_datos1 = Base_datos('Usuarios.xlsx','Sheet1')
        Usuarios = Base_datos1.leer_archivo()
        user = Usuarios.get('Usuarios')
        contrasena1 = Usuarios.get('Contrasena')
        for i in user.keys():
            if user.get(i) == self.nick:
                if contrasena1.get(i) == self.contrasena:
                    return True
        return False

    def Es_Admin(self):
        '''
        '''
        Base_datos1 = Base_datos('Usuarios.xlsx','Sheet1')
        Usuarios = Base_datos1.leer_archivo()
        user = Usuarios.get('Usuarios')
        admin = Usuarios.get('Admin')
        for i in user.keys():
            if user.get(i) == self.nick:
                if admin.get(i) == 'Si':
                    return True
        return False

    def Comprobar_User(self):
        '''
        '''
        Base_datos1 = Base_datos('Usuarios.xlsx','Sheet1')
        Usuarios = Base_datos1.leer_archivo()
        user = Usuarios.get('Usuarios')
        contra = Usuarios.get('Contrasena')
        for i in user.values():
            if self.nick == i:
                return False


        return True

    def Crear_Sesion(self):
        '''
        '''
        Base_datos1 = Base_datos('Usuarios.xlsx','Sheet1')
        Usuarios = Base_datos1.leer_archivo()
        user = Usuarios.get('Usuarios')
        num_usuarios = len(user)
        contra = Usuarios.get('Contrasena')
        user[num_usuarios] = self.nick
        contra[num_usuarios] = self.contrasena
        df2 = pd.DataFrame([[Usuarios['Usuarios'][key],Usuarios['Contrasena'][key]]for key in Usuarios['Usuarios'].keys()],
                           columns = ['Usuarios', 'Contrasena'])
        df2.to_excel('Usuarios.xlsx',
            sheet_name='Sheet1')


    def servidor(self,peli):
        HOST = socket.gethostname()
        PORT = 50111
        sock = socket.socket()
        sock.bind((HOST, PORT))
        sock.listen(5)
        (clnt, addr) = sock.accept()
        msg = sock.send(bytes(peli))
        return True

    def client(self):
        HOST = "192.168.1.186"
        PORT = 50111
        sock = socket.socket()
        sock.connect((HOST, PORT))
        msg = sock.recv(1024)
        msg_final = msg.decode("utf-8")
        return msg_final


if __name__ == '__main__':
    import doctest

    doctest.testmod()
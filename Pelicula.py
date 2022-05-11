class Punto:
    """
    Modela un punto en el espacio
    """

    def __init__(self, x=0.0, y=0.0):
        """
        Método para inicializar los objetos de la clase Punto
        >>> P = Punto(1.0, 3.0)
        >>> P.x
        1.0
        >>> P.y
        3.0
        >>> P = Punto()
        >>> P.x
        0.0
        >>> P.y
        0.0

        :param x: coordenada x
        :param y: coordenada y
        """
        self.x = x
        self.y = y

    def __sub__(self, Q):
        '''
        Sobrecarga del operador - (resta) para puntos
        >>> P = Punto(1.0, 3.0)
        >>> Q = Punto(2.0, 4.0)
        >>> R = Punto(1.0, 1.0)
        >>> Q - P == R
        True
        '''
        return Punto(self.x - Q.x, self.y - Q.y)

    def distancia(self, Q):
        """
        >>> P1 = Punto(0, 0)
        >>> P2 = Punto(1, 1)
        >>> P1.distancia(P2)
        1.4142135623730951

        :param Q: el otro punto
        :return: medida de la distancia
        """
        distx = self.x - Q.x
        disty = self.y - Q.y
        dist = (distx ** 2 + disty ** 2) ** 0.5
        return dist

    def cuadrante(self):
        """
        >>> P = Punto(1, 1)
        >>> P.cuadrante()
        1

        :return:
        """
        if self.x >= 0 and self.y >= 0:
            return 1
        elif self.x >= 0 and self.y < 0:
            return 4
        elif self.y >= 0 and self.x < 0:
            return 2
        else:
            return 3

    def modulo(self):
        '''
        Método para calcular la distancia hasta el eje de coordenadas
        >>> P = Punto(3.0, 4.0)
        >>> P.modulo()
        5.0
        '''
        return self.distancia(Punto(0, 0))

    def medio(self, Q):
        '''
        Método para obtener el punto medio entre dos puntos
        >>> P = Punto()
        >>> Q = Punto(2.0, 2.0)
        >>> P.medio(Q) == Punto(1.0, 1.0)
        True
        '''
        return Punto((self.x + Q.x) / 2, (self.y + Q.y) / 2)

    def __eq__(self, Q):
        '''
        Sobrecarga del operador == para puntos
        >>> P = Punto(1.0, 3.0)
        >>> Q = Punto(2.0, 4.0)
        >>> R = Punto(1.0, 3.0)
        >>> P == Q
        False
        >>> P == R
        True
        '''
        return self.x == Q.x and self.y == Q.y

    def get_coord_cartesianas(self):
        '''
        Método para obtener las coordenadas cartesianas (x,y)
        >>> P = Punto(4.0, 5.0)
        >>> P.get_coord_cartesianas()
        (4.0, 5.0)
        '''
        return (self.x, self.y)

    def get_coord_polares(self):
        '''
        Método para obtener las coordenadas polares (modulo, ángulo en radianes)
        Aprovecha el método modulo y usa funciones de la clase math
        >>> P = Punto(0.0, 1.0)
        >>> P.get_coord_polares()
        (1.0, 1.5707963267948966)
        '''
        from math import atan, pi
        if self.modulo() == 0.0:
            return (0.0, 0.0)
        if self.x > 0 and self.y >= 0:
            g = atan(self.y / self.x)
        elif self.x == 0 and self.y > 0:
            g = pi / 2
        elif self.x < 0:
            g = atan(self.y / self.x) + pi
        elif self.x == 0 and self.y < 0:
            g = 3 * pi / 2
        else:
            g = atan(self.y / self.x) + 2 * pi
        return (self.modulo(), g)

        if self.x == 0:
            return (self.modulo(), atan(self.y / self.x))
        elif self.modulo() != 0:
            return (self.modulo(), acos(self.x / self.modulo()))
        else:
            return (self.modulo(), asin(self.y / self.modulo()))
            # completar

        return (self.modulo(), atan2(self.y, self.x))

    def __str__(self):
        '''
        Sobrecarta de la función print para puntos
        >>> Q = Punto(2.0, 2.0)
        >>> print(Q)
        (2.0, 2.0)
        >>> Q.__str__()
        '(2.0, 2.0)'
        '''
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __neg__(self):
        '''
        Sobrecarga del operador - (cambio de signo) para puntos (x, y) -> (-x, -y)
        >>> P = Punto(2, 3)
        >>> Q = Punto(-2, -3)
        >>> -P == Q
        True
        '''
        return Punto(-self.x, -self.y)

    def __add__(self, Q):
        '''
        Sobrecarga del operador + (suma) para puntos
        >>> P = Punto(1.0, 1.2)
        >>> Q = Punto(-2.4, 5.9)
        >>> S = P + Q
        >>> round(S.x, 1)
        -1.4
        >>> round(S.y, 1)
        7.1
        '''
        return Punto(self.x + Q.x, self.y + Q.y)

    def __mul__(self, n):
        '''
        Sobrecarga del operador * (producto) para puntos
        utiliza el polimorfismo con la función type()
        mira como ejemplo __add__ en Segmento.py
        cuando n es un número se multiplica el módulo del punto
        >>> P = Punto(1.0, 1.2)
        >>> print(P * 3.0)
        (3.0, 3.6)
        '''
        return Punto(self.x * n, self.y * n)

    def min_x(self, otro):
        '''
        Método para obtener la x del punto más a la izquierda
        >>> P = Punto(1.0, -2.0)
        >>> Q = Punto(-3.0, 4.0)
        >>> P.min_x(Q)
        -3.0
        '''
        return min(self.x, otro.x)

    def min_y(self, otro):
        '''
        Método para obtener la y del punto más abajo
        >>> P = Punto(1.0, -2.0)
        >>> Q = Punto(-3.0, 4.0)
        >>> P.min_y(Q)
        -2.0
        '''
        return min(self.y, otro.y)

    def max_x(self, otro):
        '''
        Método para obtener la x del punto más arriba
        >>> P = Punto(1.0, -2.0)
        >>> Q = Punto(-3.0, 4.0)
        >>> P.max_x(Q)
        1.0
        '''
        return max(self.x, otro.x)

    def max_y(self, otro):
        '''
        Método para obtener la y del punto más a la derecha
        >>> P = Punto(1.0, -2.0)
        >>> Q = Punto(-3.0, 4.0)
        >>> P.max_y(Q)
        4.0
        '''
        return max(self.y, otro.y)


if __name__ == '__main__':
    import doctest

    doctest.testmod()

class Automovil(object):
    def __init__(self, fabricante, vel_max):
        self.__fabricante = fabricante
        self.__vel_max = vel_max
    @property
    def fabricante(self):

        print("Ejecución del Método GETTER")
        return self.__fabricante

    @fabricante.setter
    def fabricante(self, nuevo_fabricante):
        print("Ejecución del Método SETTER\n")
        print("Modificando el nombre del fabricante\n")
        self.__fabricante = nuevo_fabricante
        print("El nombre del fabricante se ha modificado por")
        print(self.__fabricante)

    @fabricante.deleter
    def fabricante(self):
        print("Borrando fabricante")
        del self.__fabricante

    @property
    def vel_max(self):
        print("Ejecutando método GETTER de VEL MAX")
        return self.__vel_max
    
    @vel_max.setter
    def vel_max(self, nueva_vel_max):
        self.__vel_max = nueva_vel_max
        print("Modificando la velocidad máxima...")
        print("La velocidad máxima en km/h ahora es:")
        print(self.__vel_max)

    @vel_max.deleter
    def vel_max(self):
        print("Borrando el valor de velocidad máxima...")
        del self.__vel_max


Porshe = Automovil("Carrera 911", 350)
print(Porshe.fabricante)
Porshe.fabricante = "Cayman"
print(Porshe.fabricante)
Porshe.vel_max = 300
del Porshe.fabricante







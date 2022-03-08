# def funcion_decoradora(funcion):
#     def wrapper():
#         print("Este es el último mensaje...")
#         funcion()
#         print("Este es el primer mensaje ;)")

#     return wrapper

# def zumbido():
#     print("Buzzz")

# zumbido = funcion_decoradora(zumbido)


# @funcion_decoradora

# def zumbido():
#     print("Buzzz")

#creación de la clase millas
# class Millas:
#     def __init__(self, distancia=0):
#         self.distancia = distancia

#     def convertir_a_kilometros(self):
#         return(self.distancia*1.609344)

# #creacion del objeto avion
# avion = Millas()

# #indicación de la distancia

# avion.distancia = 200

# #obtención del atributo distancia
# print(avion.distancia)
# #200

# #obtención del metodo convertir a kilometros

# print(avion.convertir_a_kilometros())
# #321.68688

# class Millas: 
#     def __init__(self, distancia =0):
#         self.distancia = distancia

#     def convertir_a_kilometros(self):
#         return(self.distancia*1.609344)
    
#     #metodo Getter

#     def obtener_distancia(self):
#         return self.obtener_distancia

#     #metodo setter

#     def definir_distancia(self, valor):
#         if valor < 0:
#             raise ValueError("No es posible convertir distancias menores a 0.")
#         self._distancia = valor

# #función property

# class Millas:
#     def __init__(self):
#         self.distancia = 0

#     #función para obtener el valor de _distancia
#     def obtener_distancia(self):
#         print("Llamada al método getter")
#         return self.obtener_distancia
    
#     #Función para definir el valor de _distancia
#     def definir_distancia(self, recorrido):
#         print("Llamada al método setter)")
#         self._distancia = recorrido
    
#     #Función para eliminar el atributo _distancia
#     def eliminar_distancia(self):
#         del self.distancia

#     distancia = property(obtener_distancia, definir_distancia, eliminar_distancia)


# #Crear un nuevo objeto
# avion = Millas()

# #indicar la distancia

# avion.distancia = 200

# print(avion.distancia)
# #llamada al metodo getter
# #llamada al metodo setter
# #200

#decorador @property

class Millas:
    def __init__(self):
        self._distancia = 0
    
    #Función para obtener el valor de _distancia
    #usando el decorador property
    @property
    def obtener_distancia(self):
        print("Llamada al método getter")
        return self._distancia
    
    #Función para definir el valor de _distancia
    @obtener_distancia.setter
    def definir_distancia(self, valor):
        if valor < 0:
            raise ValueError("No es posible convertir distancias menores a 0.")
        print("Llamada al método setter")
        self._distancia = valor

#creación del objeto

avion = Millas()

#indicamos distancia

avion.definir_distancia = 200
print(avion.definir_distancia)

#llamada al metodo getter
#llamada al metodo setter
#200
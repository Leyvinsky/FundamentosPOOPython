# class Persona:

#     def __init__(self, nombre, edad):
#         self.nombre = nombre
#         self.edad = edad

#     def saluda(self, otra_persona):
#         return f"Hola {otra_persona.nombre}, me llamo {self.nombre}"
        
# david = Persona("David", 35)
# erika = Persona("erika", 33)
# david.saluda(erika)
    
class Coordenada:

    def __init__(self, x , y):
        self.x = x
        self.y = y

    def distancia(self, otrac_coordenada):
        x_diff = (self.x -otrac_coordenada.x)**2
        y_diff = (self.y -otrac_coordenada.y)**2

        return(x_diff + y_diff)**0.5

if __name__ == "__main__":

    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    #print(coord_1.distancia(coord_2))
    #print(isinstance(coord_2, Coordenada))
    print(isinstance(3, Coordenada))
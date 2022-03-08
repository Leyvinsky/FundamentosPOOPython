def decorador(func2): #definimos el decorador con la función argumento func2
    def nueva_funcion(self, presentacion): #definimos la nueva función con los parametros que llevara la funcion func2
        print("El profesor comenta:") #codigo del decorador
        func2(self, presentacion) #Agregamos los parametros con los que trabaja 
    return nueva_funcion #regresa la nueva funcion 

class profesor(object): #se crea la clase heraedando object
    def __init__(self, nombre): #Constructor con el atributo nombre
        self.nombre = nombre 
    
    @decorador #se coloca el decorador antes del metodo
    def ensena(self, presentacion): #Metodo enseñar del objeto profesor
        self.presentacion = presentacion
        print(presentacion) #imprime el mensaje del objeto
        print("Hoy aprenderemos a programar en Python")

utonio = profesor("Utonio") #instanciamos
utonio.ensena("Bienvenido a tu curso de programación") # al llamar al metodo ensena añadira el decorador
#es decir en el decorador se debe incluir la instanciación self y el argumento presentación
# para nueva función y func2





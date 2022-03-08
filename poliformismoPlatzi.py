class Persona: 
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print("Caminando paso a pasito, sueve suavecito")

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)
    
    def avanza(self):
        print("Ni le das perro")

def main():
    persona = Persona("David")
    print("Me llamo", persona.nombre, "y estoy caminado")
    persona.avanza()
    ciclista = Ciclista("Daniel")
    print("Me llamo", ciclista.nombre, "y estoy pedaleando")
    ciclista.avanza()

if __name__=="__main__":
    main()

        

class CasillaDeVotacion:
    def __init__( self, identificador,pais):
        self.__identificador = identificador
        self.__pais = pais
        self.__region = None

    @property
    def region(self):
        print("Ejecución del metodo GETTER")
        return self.__region

    @region.setter
    def region(self, region):
        print("Ejecución del método SETTER")
        if region in self.__pais:
            self.__region = region
        else:
                raise ValueError(f"La región {region} no es valida en {self.__pais}")

casilla = CasillaDeVotacion(123, ["Ciudad de México", "Morelos"]) 

print(casilla.region)

casilla.region = "Ciudad de México"
print(casilla.region)

casilla.region

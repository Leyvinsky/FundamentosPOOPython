monedas = int(input("¿Cuántas monedas tienes?"))
siguiente = monedas + 1
print("Yo tengo más. Tengo", siguiente, )
                 
t = float(input("¿En cuantos segundos corres 100m?"))
dif = t - 9.58
print("Eres ", dif, "segundos más lento que Bolt")

ingreso = bool(input("Ingresa tu nombre: "))
print("Nombre ingresado: ", ingreso)

suma = 3 + 18 / 3
print(suma)

resultado = ""
distancia = 10
tiempo = 2
kilometros = 0
metros = 0
kilometros = (distancia/tiempo) * 3600
metros = (distancia/tiempo) * 1000
resultado = "La velocidad es" + str(kilometros) + "km/h o " + str(metros) + "m/s"
print(resultado)

xor = False
a = False
b = False
xor = (a or b) and not(a and b)
print(xor)

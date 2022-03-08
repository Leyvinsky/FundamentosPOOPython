def promedio_std(lista):
    if len(lista) < 2:
        return print("La lista de números es muy corta para calcular la desviación estandar\nIntenta con una lista valida")
    else:    
        x = sum(lista)/len(lista)
        y = sum((numero-x)**2 for numero in lista)
        y = y/len(lista)
        y = y**0.5
        return x, y

def color_frecuente(lista):
    orden_colores = ["azul", "rojo", "verde", "amarillo"]
    frecuencias = []

    #for color in colores:
    #    if color in frecuencias:
    #        frecuencias[color] = frecuencias[color] + 1
    #    else: 
    #        frecuencias[color] = 1
    for i in orden_colores:
        numero = 0
        for color in lista:
            if i == color:
                numero = numero + 1                
        frecuencias.append([numero, i])
    print(frecuencias)        
    #valor_mayor = max(frecuencias.values())
    #modas = [key for key, value in frecuencias.items()  if value == valor_mayor]

    #if len(modas)>1:
    #    modas = min(modas, key=lambda x: orden_colores.index())
    #else:
    #    modas = modas[0]
    #return modas, valor_mayor
    azul = frecuencias.pop()
    rojo = frecuencias.pop()
    verde = frecuencias.pop()
    amarillo = frecuencias.pop()

    if ((azul[0]>=rojo[0]) and (azul[0]>=verde[0]) and (azul[0]>=amarillo[0])):
        return (azul[1], azul[0])
    elif ((rojo[0]>azul[0]) and (rojo[0]>=verde[0]) and (rojo[0]>=amarillo[0])):
        return (rojo[1], rojo[0])
    elif ((verde[0]>azul[0]) and (verde[0]>rojo[0]) and (verde[0]>=amarillo[0])):
        return (verde[1], verde[0])
    elif ((amarillo[0]>azul[0]) and (amarillo[0]>rojo[0]) and (amarillo[0]>verde[0])):
        return (amarillo[1], amarillo[0])

def color_frecuente2(lista):
    orden_colores = ["azul", "rojo", "verde", "amarillo"]
    frecuencias = {}
    for color in lista:
        if color in frecuencias:
            frecuencias[color] = frecuencias[color] + 1
        else: 
            frecuencias[color] = 1            
    valor_mayor = max(frecuencias.values())    
    string = [key for key, value in frecuencias.items()  if value == valor_mayor]    
    if len(string)>1:    
        string= min(string, key= lambda x: orden_colores.index(x))        
    else:
        string = string[0]
    return string, valor_mayor
    
def buscaminas(tablero, i, j):
    numero_bombas=0
    for horizontal in range(i-1, i+2):
        for vertical in range(j-1, j+2):
            if horizontal<0 or horizontal>len(tablero[0])-1 or vertical<0 or vertical>len(tablero)-1:
                continue
            numero_bombas=numero_bombas+1 if tablero[horizontal][vertical]=="X" else numero_bombas
    
    return numero_bombas

#lista = [12, 14, 5, 8]
#print(promedio_std(lista))
#colores = ['verde', 'azul', 'rojo', 'amarillo', 'rojo', 'verde','amarillo']
#print(color_frecuente2(colores))
#colores2 = ['amarillo', 'verde', 'rojo', 'azul', 'verde', 'rojo', 'azul', 'amarillo'] 
#print(color_frecuente2(colores2))
#colores3 = ['rojo', 'verde', 'azul', 'amarillo', 'rojo', 'verde']
#print(color_frecuente2(colores3))
#colores4 = ['rojo', 'verde', 'azul', 'amarillo', 'rojo', 'rojo']
#print(color_frecuente2(colores4))
tablero_4_4 = ['','X','','X'],['X','','',''],['','X','X',''],['X','','','X']
print(tablero_4_4)
x,y = 0, 0
print(buscaminas(tablero_4_4, x, y))
x,y = 1, 1
print(buscaminas(tablero_4_4, x, y))

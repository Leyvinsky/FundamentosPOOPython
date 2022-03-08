#busqueda binaria
#división y conquista
#iteraciones
#si la lista no esta ordenada, busqueda lineal
#si esta ordenada busqueda binaria
import random

def busqueda_lineal(lista, objetivo, contador_lineal=0):
    match = False

    for elemento in lista:
        contador_lineal += 1
        if elemento == objetivo:
            match = True
            break

    return (match, contador_lineal)

def busqueda_binaria(lista, comienzo, final, objetivo, contador = 0):
    contador += 1
    print(f'Buscaando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return (False, contador)
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, contador)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, contador = contador)
    
    else:
        return busqueda_binaria(lista, comienzo, medio -1, objetivo, contador = contador)


if __name__ == "__main__":
    tamano_de_lista = int(input("¿De que tamaño será la lista?"))
    objetivo = int(input("Que número quieres encontrar?"))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    (encontrado, contador_binario) = busqueda_binaria(lista, 0, len(lista), objetivo)
    (encontrado, contador_lineal) = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} { "esta" if encontrado else "no esta"} en la lista')
    print(f'Iteraciones Busqueda binaria {contador_binario}')
    print(f'Iteraciones Busqueda lineal {contador_lineal}')

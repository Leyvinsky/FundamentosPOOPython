def mezclador(string_a, string_b):
    if len(string_a) > 2 and len(string_b) >2:
        a = string_a[0:2]
        b = string_b[-2:]
        c = a + b
        return c
    elif len(string_a) <= 2 and len(string_b) > 2:
        return print("La primer palabra es muy corta")

    elif len(string_a) > 2 and len(string_b) <= 2:
        return print("La segunda palabra es muy corta")
    else:
        return print("Ambas palabras son muy cortas")

def intercalar(string_a, string_b):
    newstring= ""
    i = 0
    while i < len(string_a):
        newstring = newstring + string_a[i] + string_b
        i += 1
    return newstring


def ocurrencias(string):
    cero = 0
    uno = 0
    for i in string:
        if i == "1":
            uno=uno+1
        elif i == "0":
            cero = cero + 1     
    
    return uno-cero

def remover_enesimo(s, n):
    newstring = ""
    if n == 0:
        newstring = s[1:]
    elif n == len(s)-1:
        newstring = s[0:len(s)-1]
    
    elif n >= len(s):
        print("Elije un numero que sea menor que la cantidad de caracteres de la cadena ingresada ")
    else:
        newstring = s[0:n] + s[n+1:]
    return newstring

def reemplazo(string):
    newstring = ""
    mayusculas = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for letra in string:
        if letra in mayusculas:
            newstring = newstring + "$"
        else:
            newstring = newstring + letra
    return newstring
#cadena_a=input(print("ingresa una palabra "))
#cadena_b=input(print("ingresa otra palabra"))
#print(mezclador(cadena_a,cadena_b))
#cadena_a=input(print("Inserte una cadena: "))
#cadena_b=input(print("Inserte otra cadena: "))
#print(intercalar(cadena_a, cadena_b)) 
cadena_a=input(print("Ingresa una cadena: "))
print(ocurrencias(cadena_a))
#cadena_a=input(print("Ingresa una cadena: "))
#indice=int(input(print("Ingresa un numero")))
#print(remover_enesimo(cadena_a, indice))
#cadena_a=input(print("ingresa una palabra: "))
#print(reemplazo(cadena_a))

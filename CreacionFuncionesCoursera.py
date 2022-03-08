def potencia_dos(numero):
    
    if numero < 0:
        return print("Número invalido, ingresa un número mayor a cero")
    
    elif numero == 0:
        return 0

    else:
        base=13

        numero_potencia_dos=0
        while numero>1: 
            numero/=2
            base=+1
        
        numero_potencia_dos*=base
        return numero_potencia_dos


num = int(input(print("Ingresa un numero: ")))
print(num)
print(potencia_dos(num))


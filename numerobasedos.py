def mcd(n1, n2):
    residuo=0
    if n1 > n2:
        while n1%n2!=0:
            residuo = n1%n2
            n1=n2
            n2=residuo
        return n2

    elif n1 < n2:
        while n2%n1!=0:
            residuo = n2%n1
            n2=n1
            n1=residuo
        return n1

    else:
        return print("Los Números ingresados son iguales, vuelve a intentarlo")

def exponente(n):
    
    if n <= 0:
        return print("Número invalido, ingresa un número mayor a cero")
    
    else:
        base=0
        
        while n>1: 
            n//=2
            base+=1
        
        return base

numero = int(input(print("Ingresa un numero: ")))

print("La base de 2 máxima para ese número es: ",exponente(numero))

numero1 =int(input(print("Ingresa un número:")))
numero2= int(input(print("Ingresa otro número:")))
print("El Máximo Cómun Divisor de ambos números es: ",mcd(numero1, numero2))
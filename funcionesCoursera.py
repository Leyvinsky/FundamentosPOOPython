
#variables locales son las que solo existen dentro de la función donde se definen
def funcionmisteriorsa(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def funcion2(y):
    c=0
    while y!=0:
        c+=1
        y = y // 10
    return c

def potencia(base, exponente):
    if exponente ==0:
        return 1
    else:
        resultado = 1
        while exponente > 0:
            resultado *= base
            exponente -= 1
        return resultado


def max_div(n):
    max_actual = 0
    i=1
    while i < n:
        if n%i==0:
            max_actual =i
            
        i += 1
        
        
    return max_actual

b=102
print(funcionmisteriorsa(b))

b=103
print(funcionmisteriorsa(b))

d = 78907566544
print(funcion2(d))

#numero =int(input("ingresa un numero: "))
#print(max_div(numero))

basei =int(input("ingresa un numero: "))
exponentei =int(input("ingresa otro numero: "))


print(potencia(basei, exponentei))

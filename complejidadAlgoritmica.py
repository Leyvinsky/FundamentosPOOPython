import time
import sys

sys.setrecursionlimit(2000000)

#implementacion recursiva e iterativa
def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta

def factorial_recursivo(n):
    if n == 1:
        return 1
    else:
        return n * factorial_recursivo(n-1)

if __name__ == "__main__":
    n = 10000
    

    comienzo= time.time()
    #print(factorial(n))
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    #print(factorial_recursivo(n))
    factorial_recursivo(n)
    final = time.time()
    print(final - comienzo)


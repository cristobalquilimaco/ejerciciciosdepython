# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def es_primo(num):
    #Aqui se determina si un numero es primo 
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1): #El bucle comienza en 2 porque es el numero divisible 
        if num % i == 0: #Aqui valido si el numero dividido entre el indice es igual a 0
            return False
    return True

numero = int(input("Ingresa el numero para verificar se es primo"))
if es_primo(numero):
    print(f"{numero} es un numero primo")
else:
    print(f"{numero} no es un numero primo")

print("Números primos entre 1 y 100:")
primos = [n for n in range(1, 101) if es_primo(n)]
print(primos)
# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

def es_primo():
    #Aqui se determina si un numero es primo 
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
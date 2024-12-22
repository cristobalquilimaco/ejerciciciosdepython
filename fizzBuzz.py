# Ejercicio: Fizz Buzz
# Escribe un programa en Python que haga lo siguiente:

# Iterar sobre los números del 1 al 100 (ambos inclusive).
# Para cada número:
# Imprimir "Fizz" si el número es divisible por 3.
# Imprimir "Buzz" si el número es divisible por 5.
# Imprimir "FizzBuzz" si el número es divisible por ambos (3 y 5).
# Imprimir el número si no es divisible por 3 ni por 5.

def fizz_buzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)

fizz_buzz()
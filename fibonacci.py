# Enunciado del ejercicio:

# La sucesión de Fibonacci es una serie de números donde cada número es la suma de los dos anteriores. 
# La secuencia comienza con 0 y 1,

# Tu tarea es escribir un programa en Python que:

# Solicite al usuario un número entero 
# 𝑛
# n.
# Calcule los primeros 
# 𝑛
# n números de la sucesión de Fibonacci.
# Imprima la secuencia resultante.


# Tareas:
# Completa la función generar_fibonacci para que calcule correctamente la sucesión.
# Prueba el código con diferentes valores de entrada para asegurarte de que funciona.

def generar_fibonacci():
    # genera los primeros numeros n de la sucesion fibonacci
    return []

#Solicitar el numero al usuario

n = int(input("Ingresa un numero en terminos de la sucesion fibonacci: "))

#Validar que el numero sea positivo

if n <= 0:
    print("Por favor, ingresa un numero entero positivo")

else:
    #Llamar a la funcion y mostrar el resultado
    fibonacci = generar_fibonacci()
    print(f"los numeros {n} terminos de la sucesion fibonacci son: {fibonacci}")
#Estructura List Comprehension: [Expresion for elemento in iterable if condicion]

#EXPRESION: es lo que se va a incluir en la nueva lista. Puede ser el mismo elemento
#ELEMENTO: Es la variable que toma cada valor del iterable
#ITERABLE: Es la secuencia de la cual se toman los elementos(listas, tuplas, rango, etc)
#IF CONDICION: (opcional): Filtra los elementos que se incluiran en la nueva lista.


#Lo primero que se coloca es la formula o lo que queremos aplicar 


squares = [x ** 2 for x in range(1, 11) ] #X va a ser el valor que va a tener cada uno de los elementos, luego se aplica el for para que aplique la formula a todos los elementos
# print(f"Los cuadrados son: ", squares)


celsius = [0,10,20,30,40]
farenheit = [(temp * 9/5) *32 for temp in celsius]

# print(f"La temperatura actual es de: {farenheit}")

evens = [x for x in range(1, 21) if x%2 ==0]
# print(evens)


matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]
          ]

tranposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]

print(matrix)
for row in tranposed:
    print(row)
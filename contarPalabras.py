# Escribe una función llamada contar_palabras que reciba una cadena de texto como argumento y devuelva un diccionario donde las claves sean las palabras únicas y los valores representen la cantidad de veces que aparece cada palabra en el texto.

# Requisitos:

# Ignorar mayúsculas y minúsculas (es decir, "Hola" y "hola" cuentan como la misma palabra).
# Ignorar signos de puntuación como comas, puntos, signos de exclamación o interrogación.
# Devolver el diccionario ordenado alfabéticamente por las palabras.

import re
from collections import Counter

def contar_palabras(texto):
    texto = texto.lower()
    palabras = re.findall(r'\b\w+\b', texto)

    frecuencia = Counter(palabras)

    return dict(sorted(frecuencia.items()))


texto = "Hola, hola! ¿Cómo estás? Espero que estés bien. Hola otra vez."
resultado = contar_palabras(texto)
print(resultado)

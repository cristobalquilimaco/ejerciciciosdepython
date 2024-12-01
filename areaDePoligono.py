"""
 * Crea una única función (importante que sólo sea una) que sea capaz
 * de calcular y retornar el área de un polígono.
 * - La función recibirá por parámetro sólo UN polígono a la vez.
 * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
 * - Imprime el cálculo del área de un polígono de cada tipo.
 */
"""

def calcularAreaPoligono(poligon_type, **params):

    if poligon_type == "triangulo":
        base = params.get("base")
        altura = params.get("altura")
        if base and altura:
            return(base * altura) / 2
        return "Faltan areas en el triangulo"
    
    elif poligon_type == "cuadrado":
        lado = params.get("lado")
        if lado:
            return lado **2
        return "Faltan lados en el"

    
    elif poligon_type == "rectangulo":
        base = params.get("base")
        altura = params.get("altura")
        if base and altura:
            return base * altura
        return "Faltan dimensiones para calcular el rectangulo"
    
    else:
        return "Tipo de poligono no soportado"

area_triangulo = calcularAreaPoligono("triangulo", base=10 , altura=5)
area_cuadrado = calcularAreaPoligono("cuadrado", lado=3 )
area_rectangulo = calcularAreaPoligono("rectangulo", base=30, altura= 4)

print(f"El area del triangulo es igual a: {area_triangulo}")
print(f"El area del cuadrado es igual a: {area_cuadrado}")
print(f"El area del rectangulo es igual a: {area_rectangulo}")
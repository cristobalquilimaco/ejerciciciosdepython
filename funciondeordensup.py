#ejercicio#
'''Tienes una lista de productos con su nombre y precio. Debes realizar las siguientes tareas:
Crear dos funciones que apliquen diferentes descuentos a los precios de los productos (10% de desccuento y 20% de descuento).
Crear una función de orden superior que tome una lista de productos y una función de descuento, y aplique ese descuento a todos los productos.
Usar la función de orden superior con las funciones de descuento para obtener listas de productos con los precios descontados.'''



products = [
    {"nombre": "medias", "precio": 10.00},
    {"nombre": "hoodie", "precio": 35.00},
    {"nombre": "shirt", "precio": 40.00},
    {"nombre": "pantalon", "precio": 60.00},
    {"nombre": "sweater", "precio": 50.00},
]

def discount_ten(precio):
    return precio - (precio * 10 / 100)

def discount_twenty(precio): 
    return precio - (precio * 20 / 100)

def discount_productos (todos_productos, discount_of_productos):
    for product in todos_productos:
        product["precio"] = discount_of_productos(product["precio"])
        return products
        

print(discount_productos(products, discount_ten))







"""products = [
    {"nombre": "medias", "precio": 10.00},
    {"nombre": "hoodie", "precio": 35.00},
    {"nombre": "shirt", "precio": 40.00},
    {"nombre": "pantalon", "precio": 60.00},
    {"nombre": "sweater", "precio": 50.00},
]

def discount_ten(precio):
    #Calculas el monto del descuento y luego lo restas del precio original#
    return precio - (precio * 10 / 100)

def discount_twenty(precio): 
    return precio - (precio * 20 / 100)

def apply_discount_to_products(all_products, discount_fun):
     return [
     {"nombre": product["nombre"], "precio": discount_fun(product["precio"])}
        for product in all_products
        ]

print(apply_discount_to_products(products, discount_ten))
print(apply_discount_to_products(products, discount_twenty))
"""

products = [
    {"nombre": "medias", "precio": 10.00},
    {"nombre": "hoodie", "precio": 35.00},
    {"nombre": "shirt", "precio": 40.00},
    {"nombre": "pantalon", "precio": 60.00},
    {"nombre": "sweater", "precio": 50.00},
]




"""solucion con append

def discount_ten(price):
    return price - (price * 10 / 100)

def discount_twenty(price):
    return price - (price * 20 / 100)

def apply_discount_to_products(products, discount_fun):
    discounted_products = []  # Inicializa una lista vacía

    for product in products:
        new_price = discount_fun(product["precio"])  # Aplica el descuento
        discounted_product = {"nombre": product["nombre"], "precio": new_price}  # Crea el nuevo diccionario
        discounted_products.append(discounted_product)  # Agrega el nuevo diccionario a la lista
    
    return discounted_products

# Aplicar descuentos y imprimir resultados
print(apply_discount_to_products(products, discount_ten))
print(apply_discount_to_products(products, discount_twenty))"""
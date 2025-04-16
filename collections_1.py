from collections import defaultdict

def count_products(orders: list[str]) -> defaultdict:
    #crea un idccionario con valor por defecto 0
    product_count = defaultdict(int)
    for product in orders:
        product_count[product] +=1
        
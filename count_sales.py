from collections import Counter

def counter_sales(products: list[str]) ->Counter:
    #Usa Counter para contar cuantos productos de cada tipo se han vendido
    return Counter(products)

sales = ["laptop", "smartphone", "laptop", "tablet"]
result = counter_sales(sales)
print(result)
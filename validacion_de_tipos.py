# def divide(a: int, b: int) -> float:
#     return a/b

# print(divide(10, "2"))

def divide(a: int, b: int) -> float:

    if isinstance(a, int) or not isinstance(b, int):
        print('Error: ambos parametros deben ser enteros o flotantes')
        return None
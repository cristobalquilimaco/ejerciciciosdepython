class Person():
    def __init__(self, nombre: str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        #devuelve una representacion amigable del producto
        return f"Persona: {self.nombre}, {self.edad} años"
    
    
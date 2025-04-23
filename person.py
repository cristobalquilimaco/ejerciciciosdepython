class Person():
    def __init__(self, nombre: str, edad:int):
        self.nombre = nombre
        self.edad = edad

    def __str__(self) -> str:
        #devuelve una representacion amigable del producto
        return f"Persona: {self.nombre}, {self.edad} años"
    
    def __eq__(self) -> str:
        #Devuelve una representacion detallada del objeto para la depuración
        return f"Persona(nombre='{self.nombre}', edad={self.edad})"
    
    
#SISTEMA DE GESTION PARA BIBLIOTECAS
#Crear clases para representar libros y miembros de una biblioteca

class Libro:
    def __init__(self, titulo, autor, anio_publicacion, isbn):
        self.titulo = titulo
        self.autor = autor
        self.anio_publicaion = anio_publicacion
        self.isbn = isbn
        self.prestado = False

    def prestamo(self):
        self.prestamo = True

    def devolucion(self):
        self.prestamo = False

class Miembro:
    def __init__(self, nombre, numero_miembro):
        self.nombre = nombre
        self.numero_miembre = numero_miembro
        self.libros_prestados = []

    def prestar_libro(self, libro):
        if not libro.prestado:
            libro.prestamo()
            self.libros_prestados.append(libro)
        
        else:
            print(f"El libro {libro.titulo} ya esta prestado")


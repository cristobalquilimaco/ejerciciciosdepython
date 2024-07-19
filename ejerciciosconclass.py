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

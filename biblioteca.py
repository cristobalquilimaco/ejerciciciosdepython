class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no esta disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = [] #lista

    def borrow_books(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"el libro {book.title} no esta disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no esta en la lista de prestados")

class Library:
    def __init__(self):
        self.users = []
        self.book = []

    def add_book(self, book):
        self.book.append(book)
        print(f"el libro {book.title} ha sido agregado")
    
    def register_user(self, user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")

    def show_available_books(self):
        print("Los libros disponibles:")
        for book in self.book:
            if book.available:
                print(f"{book.title} por {book.author}")

# Crear los libros
book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("1994", "George Orwell")

#Crear Usuario
user1 = User("Carli", "001")

#Crear la biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.register_user(user1)

# MOSTRAR LIBROS
library.show_available_books()


#REALIZAR PRESTAMOS
user1.borrow_books(book1)
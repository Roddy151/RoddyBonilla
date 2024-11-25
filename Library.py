class Book:
    def __init__(self, title, author):
        self.title  = title
        self.author  = author
        self.available = True
    
    def borrow(self):
        if self.available:
            self.available = False
            print(f"El libro {self.title} a sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")
    
    def returnBook(self):
        self.available = True
        print(f"El libro {self.title} a sido devuelto")

class User():
    def __init__(self, name, userId):
        self.name = name
        self.userId = userId
        self.borrowedBooks = []
        
    
    def borrowedBook(self, book):
        if book.available:
            book.borrow()
            self.borrowedBooks.append(book)
            print(f"El libro {book.title} a sido prestado por {self.name}")
        else:
            print(f"El libro {book.title} no está disponible")

    def returnBook(self, book):
        if book in self.borrowedBooks:
            book.returnBook()
            self.borrowedBooks.remove(book)
            print(f"El libro {book.title} a sido devuelto por {self.name}")
        else:
            print(f"El libro {book.title} no está en la lista por {self.name}")
    
class Library:
    def __init__(self):
        self.books = []
        self.user = []

    def addBooks(self, book):
        self.books.append(book)
        print(f"El libro {book.title} a sido agregado")

    def registerUser(self, user):
        self.user.append(user)
        print(f"Se ha registrado el usuarios {user.name}")    
    
    def showAvailableBook(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")

#crear libros            
book1 = Book("El Principito", "Antoine de Saint-Exupéry")
book2 = Book("El Hobre más Rico de Babilonia", "George S. Clason")

#crear usuarios

user1 = User("Anissa Bonilla", "001")
user2 = User("Roddy Bonilla", "002")
user3 = User("Anlly Cárdenas", "003")

#Crear biblioteca

library=Library()
library.addBooks(book1)
library.addBooks(book2)
library.registerUser(user1)
library.registerUser(user2)
library.registerUser(user3)

#Mostrar Libros

library.showAvailableBook()

#Realizar prestamo

user1.borrowedBook(book1)
user3.borrowedBook(book2)

#Mostrar Libros
library.showAvailableBook()

#Entregar libros

user3.returnBook(book2)
user1.returnBook(book1)

#moatrar libros

library.showAvailableBook()
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            return True
        else:
            return False

    def return_book(self):
        self.is_available = True


class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed the book '{book.title}' by {book.author}.")
        else:
            print(f"The book '{book.title}' by {book.author} is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned the book '{book.title}' by {book.author}.")
        else:
            print(f"{self.name} did not borrow the book '{book.title}' by {book.author}.")

    def display_borrowed_books(self):
        if self.borrowed_books:
            print(f"{self.name}'s borrowed books:")
            for book in self.borrowed_books:
                print(f"Title: {book.title}")
                print(f"Author: {book.author}")
                print(f"Availability: {'Available' if book.is_available else 'Borrowed'}")
                print()
        else:
            print(f"{self.name} has not borrowed any books.")


# Membuat objek LibraryMember
member1 = LibraryMember("John")

# Membuat beberapa objek Book
book1 = Book("Python Programming", "John Smith")
book2 = Book("Data Science 101", "Emily Brown")
book3 = Book("Web Development Basics", "David Johnson")

# Meminjam buku oleh member1
member1.borrow_book(book1)
member1.borrow_book(book2)

# Menampilkan daftar buku yang dipinjam oleh member1
member1.display_borrowed_books()

# Mengembalikan salah satu buku
member1.return_book(book1)

# Menampilkan daftar buku setelah pengembalian
member1.display_borrowed_books()

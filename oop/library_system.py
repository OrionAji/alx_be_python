class Book:
    def __init__(self, title=str, author=str):
        self.title = title
        self.author = author
    
class Ebook(Book):
    def __init__(self, title=str, author=str, file_size=float):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

class PrintBook(Book):
    def __init__(self, title=str, author=str, page_count=int):
        super().__init__(title, author)
        self.page_count = page_count
        
class Library:
    def __init__(self):
        self.books = [Book, Ebook, PrintBook]
    
    def add_book(self, book: Book):
        self.books.append(book)
    
    def list_books(self):
        for book in self.books:
            if isinstance(book, Ebook):
                print(f"Ebook: {book.title} by {book.author}, Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"Print Book: {book.title} by {book.author}, Pages: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
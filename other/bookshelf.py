# Books and Bookshelf challenge

class Book:
    def __init__(self, title: str, author: str, publisher: str, pub_year: int):
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pub_year = pub_year
    
    def __str__(self):
        return (f"Title: {self.title}\n"
                f"Author: {self.author}\n"
                f"Publisher: {self.publisher}\n"
                f"Publication Year: {self.pub_year}")

class Magazine(Book):
    def __init__(self, title: str, author: str, publisher: str, pub_year: int, issue: str):
        super().__init__(title, author, publisher, pub_year)
        self.issue = issue
    
    def __str__(self):
        return (super().__str__() + f"\nIssue: {self.issue}")

class BookShelf:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.books = []
    
    def add_book(self, book: Book):
        if not isinstance(book, Book):
            print("Only books or its subclasses can be added to the bookshelf.")
            return
        
        if len(self.books) < self.capacity:
            self.books.append(book)
            print(f"'{book.title}' has been added to the shelf.")
        else:
            print(f"The shelf is full. Cannot add '{book.title}'.")
    
    def remove_book(self, book: Book):
        if book in self.books:
            self.books.remove(book)
            print(f"'{book.title}' has been removed from the shelf.")
        else:
            print(f"'{book.title}' is not on the shelf.")
    
    def find_book_by_title(self, title: str) -> Book:
        for book in self.books:
            if book.title == title:
                print(book)
                return
        print(f"No book with title '{title}' is on the shelf.")
        return None
    
    def find_books_by_author(self, author: str) -> list:
        books_by_author = [book for book in self.books if book.author.lower() == author.lower()]
        if not books_by_author:
            print(f"No books by author '{author}' are on the shelf.")
        else:
            for book in books_by_author:
                print(book)
        return 
    
    def __str__(self):
        if not self.books:
            return "The shelf is empty."
        else:
            output = "Books on the shelf:\n"
            for book in self.books:
                output += str(book) + "\n\n"
            return output.strip()


book1 = Book("1984", "George Orwell", "Secker & Warburg", 1949)
magazine = Magazine("National Geographic", "Various", "National Geographic Society", 2022, "January")
print(book1)
shelf = BookShelf(2)
print(shelf)

shelf.add_book(book1)
print(shelf)

#shelf.remove_book(book1)
#print(shelf)

shelf.add_book(magazine)
print(shelf)

shelf.find_book_by_title("1984")


shelf.find_books_by_author("George Orwell")




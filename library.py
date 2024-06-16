# Example of Book class implementation
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return True
        return False

class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books and book.return_book():
            self.borrowed_books.remove(book)
            return True
        return False

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def register_member(self, member):
        self.members.append(member)

    def borrow_book(self, book, member):
        if member.borrow_book(book):
            self.books.remove(book)
            return True
        return False

    def return_book(self, book, member):
        if member.return_book(book):
            self.books.append(book)
            return True
        return False
# Example usage
if __name__ == "__main__":
    # Create books
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "0987654321")
    book3 = Book("1984", "George Orwell", "1122334455")

    # Create members
    member1 = Member("Alice", 1)
    member2 = Member("Bob", 2)

    # Create a library
    library = Library("City Library")

    # Add books to the library
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Register members
    library.register_member(member1)
    library.register_member(member2)

    # Borrow and return books
    print("Borrowing Book 1 for Alice:", library.borrow_book(book1, member1))  # Should return True
    print("Borrowing Book 1 for Bob:", library.borrow_book(book1, member2))    # Should return False (already borrowed by Alice)
    print("Returning Book 1 for Alice:", library.return_book(book1, member1))  # Should return True
    print("Borrowing Book 1 for Bob again:", library.borrow_book(book1, member2))  # Should return True
    print("Borrowing Book 2 for Alice:", library.borrow_book(book2, member1))  # Should return True
    print("Borrowing Book 3 for Alice:", library.borrow_book(book3, member1))  # Should return True
    print("Returning Book 2 for Alice:", library.return_book(book2, member1))  # Should return True
    print("Returning Book 3 for Alice:", library.return_book(book3, member1))  # Should return True
    print("Returning Book 1 for Bob:", library.return_book(book1, member2))  # Should return True


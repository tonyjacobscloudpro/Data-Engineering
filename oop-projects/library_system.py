# library_system.py

# Features and Functionality:
# - Object-Oriented Design:
#   Implements a modular and maintainable system using classes for Library, Books, Members, and Transactions.
# - Book Management:
#   Add, remove, and search for books in the library.
# - Member Management:
#   Add and manage library members.
# - Book Borrowing and Returning:
#   Tracks book transactions with borrowing and returning operations.

# 1. Library System Design
# - This section defines the core classes for the library system: `Library`, `Book`, `Member`, and `Transaction`.

print("1. Library System Design")

class Book:
    """
    Represents a book in the library.
    """
    def __init__(self, book_id, title, author, copies=1):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"[{self.book_id}] {self.title} by {self.author} (Copies: {self.copies})"


class Member:
    """
    Represents a library member.
    """
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return f"[{self.member_id}] {self.name} (Borrowed: {len(self.borrowed_books)})"


class Library:
    """
    Represents the library system.
    """
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self, book):
        """
        Adds a book to the library.
        """
        if book.book_id in self.books:
            self.books[book.book_id].copies += book.copies
        else:
            self.books[book.book_id] = book
        print(f"Added {book}")

    def remove_book(self, book_id):
        """
        Removes a book from the library by its ID.
        """
        if book_id in self.books:
            del self.books[book_id]
            print(f"Removed book with ID: {book_id}")
        else:
            print(f"Book ID {book_id} not found.")

    def add_member(self, member):
        """
        Adds a new member to the library.
        """
        if member.member_id in self.members:
            print(f"Member ID {member.member_id} already exists.")
        else:
            self.members[member.member_id] = member
            print(f"Added member: {member}")

    def search_book(self, title):
        """
        Searches for a book by its title.
        """
        results = [book for book in self.books.values() if title.lower() in book.title.lower()]
        return results

    def borrow_book(self, member_id, book_id):
        """
        Allows a member to borrow a book.
        """
        if member_id not in self.members:
            print(f"Member ID {member_id} not found.")
            return
        if book_id not in self.books:
            print(f"Book ID {book_id} not found.")
            return
        if self.books[book_id].copies == 0:
            print(f"Book ID {book_id} is currently unavailable.")
            return

        member = self.members[member_id]
        book = self.books[book_id]
        member.borrowed_books.append(book)
        book.copies -= 1
        print(f"{member.name} borrowed {book.title}")

    def return_book(self, member_id, book_id):
        """
        Allows a member to return a book.
        """
        if member_id not in self.members:
            print(f"Member ID {member_id} not found.")
            return

        member = self.members[member_id]
        for book in member.borrowed_books:
            if book.book_id == book_id:
                member.borrowed_books.remove(book)
                self.books[book_id].copies += 1
                print(f"{member.name} returned {book.title}")
                return

        print(f"Book ID {book_id} not found in {member.name}'s borrowed books.")

# 2. Test the Library System
# - This section initializes the library and performs operations such as adding books, registering members, borrowing, and returning books.

print("\n2. Testing the Library System")

def test_library_system():
    # Initialize the library
    library = Library()

    # Add books to the library
    book1 = Book(book_id=1, title="The Great Gatsby", author="F. Scott Fitzgerald", copies=3)
    book2 = Book(book_id=2, title="1984", author="George Orwell", copies=2)
    book3 = Book(book_id=3, title="To Kill a Mockingbird", author="Harper Lee", copies=1)
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Add members to the library
    member1 = Member(member_id=1, name="Alice")
    member2 = Member(member_id=2, name="Bob")
    library.add_member(member1)
    library.add_member(member2)

    # Search for a book
    print("\nSearch Results for '1984':")
    search_results = library.search_book("1984")
    for book in search_results:
        print(book)

    # Borrow a book
    print("\nBorrowing Books:")
    library.borrow_book(member_id=1, book_id=1)
    library.borrow_book(member_id=2, book_id=2)
    library.borrow_book(member_id=1, book_id=3)

    # Try borrowing an unavailable book
    library.borrow_book(member_id=2, book_id=3)

    # Return a book
    print("\nReturning Books:")
    library.return_book(member_id=1, book_id=1)
    library.return_book(member_id=2, book_id=3)

    # Print member and book status
    print("\nLibrary Members:")
    for member in library.members.values():
        print(member)

    print("\nLibrary Books:")
    for book in library.books.values():
        print(book)


# Run the test
test_library_system()

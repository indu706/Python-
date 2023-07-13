class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        return f"Book ID: {self.book_id}\nTitle: {self.title}\nAuthor: {self.author}\nAvailability: {'Available' if self.is_available else 'Not Available'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                return True
        return False

    def display_books(self):
        if len(self.books) == 0:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)
                print()

    def find_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def checkout_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            print("Book not found.")
        elif not book.is_available:
            print("Book is already checked out.")
        else:
            book.is_available = False
            print("Book checked out successfully.")

    def return_book(self, book_id):
        book = self.find_book(book_id)
        if book is None:
            print("Book not found.")
        elif book.is_available:
            print("Book is already available in the library.")
        else:
            book.is_available = True
            print("Book returned successfully.")


def main():
    library = Library()

    while True:
        print("=== Library Management System ===")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Display Books")
        print("4. Checkout Book")
        print("5. Return Book")
        print("0. Exit")
        print("=================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            book_id = input("Enter book ID: ")
            book = Book(title, author, book_id)
            library.add_book(book)
            print("Book added to the library.")

        elif choice == "2":
            book_id = input("Enter book ID: ")
            if library.remove_book(book_id):
                print("Book removed from the library.")
            else:
                print("Book not found.")

        elif choice == "3":
            library.display_books()

        elif choice == "4":
            book_id = input("Enter book ID: ")
            library.checkout_book(book_id)

        elif choice == "5":
            book_id = input("Enter book ID: ")
            library.return_book(book_id)

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == '__main__':
    main()

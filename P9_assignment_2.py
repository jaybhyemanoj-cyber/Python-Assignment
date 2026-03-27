class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title):
        self.books.append(Book(title))
        print("Book added.")

    def add_member(self, name):
        self.members.append(Member(name))
        print("Member added.")

    def lend_book(self, title, member_name):
        for book in self.books:
            if book.title == title and book.available:
                for member in self.members:
                    if member.name == member_name:
                        book.available = False
                        member.borrowed_books.append(book)
                        print("Book lent successfully.")
                        return
        print("Book not available.")

    def return_book(self, title, member_name):
        for member in self.members:
            if member.name == member_name:
                for book in member.borrowed_books:
                    if book.title == title:
                        book.available = True
                        member.borrowed_books.remove(book)
                        print("Book returned.")
                        return
        print("Book not found.")

    def display_books(self):
        for book in self.books:
            status = "Available" if book.available else "Not Available"
            print(book.title, "-", status)


lib = Library()

while True:
    print("\n1.Add Book\n2.Add Member\n3.Lend Book\n4.Return Book\n5.Display Books\n6.Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        lib.add_book(input("Enter book title: "))
    elif choice == 2:
        lib.add_member(input("Enter member name: "))
    elif choice == 3:
        lib.lend_book(input("Book title: "), input("Member name: "))
    elif choice == 4:
        lib.return_book(input("Book title: "), input("Member name: "))
    elif choice == 5:
        lib.display_books()
    elif choice == 6:
        break
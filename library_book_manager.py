class Book:
    def __init__(self, title: str, author: str, copies: int):
        self.__title = title
        self.__author = author
        self.__copies = copies
        self.__borrow = 0
    
    def title(self):
        return self.__title
    
    def author(self):
        return self.__author
    
    def copies(self):
        return self.__copies
    
    def borrow_count(self):
        return self.__borrow
    
    def borrow(self):
        if self.__copies > 0:
            self.__borrow += 1
            self.__copies -= 1
            print(f"You borrowed '{self.__title}'.")
        else: 
            print("Not enough copies for this book.")
    
    def return_book(self):
        self.__copies += 1

class Library():
    def __init__(self):
        self.__books = {}
    
    def add_book(self, title: str, author: str, copies: int):
        if title not in self.__books:
            self.__books[title] = Book(title, author, copies)
    
    def borrow_book(self, title: str):
        if title in self.__books:
            self.__books[title].borrow()
        else:
            print("Book not found.")

    def return_book(self, title: str):
        if title in self.__books:
            self.__books[title].return_book()
            print(f"You have returned {title}. ")
        else:
            print("Book not found.")
    
    def all_books(self):
        for k in self.__books.values():
            print(f"{k.title()} by {k.author()} ({k.copies()} copies available)")
    
    def statistics(self):
        if not self.__books:
            print("No books added yet.")
            return
        
        total_books = len(self.__books)
        total_borrowed = sum(book.borrow_count() for book in self.__books.values())

        print(f"\nFun fact: {total_books} books have been borrowed {total_borrowed} times.")

        for book in self.__books.values():
            count = book.borrow_count()
            times = "times" if count != 1 else "time"
            print(f"{book.title()} borrowed {count} {times}.")
        
class UserInterface:
    def __init__(self):
        self.__library = Library()

    def help(self):
        print("0 exit")
        print("1 add book")
        print("2 borrow book")
        print("3 return book")
        print("4 show all books")
        print("5 statistics")

    def add_book(self):
        title = input("title: ")
        author = input("author: ")
        copies = int(input("copies: "))
        self.__library.add_book(title, author, copies)

    def borrow_book(self):
        title = input("title: ")
        self.__library.borrow_book(title)

    def return_book(self):
        title = input("title: ")
        self.__library.return_book(title)

    def show_stats(self):
        self.__library.statistics()

    def show_books(self):
        self.__library.all_books()

    def execute(self):
        self.help()
        while True:
            print("")
            command = input("command: ")
            if command == "0":
                break
            elif command == "1":
                self.add_book()
            elif command == "2":
                self.borrow_book()
            elif command == "3":
                self.return_book()
            elif command == "4":
                self.show_books()
            elif command == "5":
                self.show_stats()
            else:
                self.help()

if __name__ == "__main__":
    application = UserInterface()
    application.execute()

class Library:
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lendDict = {}

    def displayBook(self):
        print(f"We have the following books available in {self.name} :)")
        for book in self.bookslist:
            print(book)

    def lendBook(self, user, book):
        # if book not in self.bookslist():
        #     print("Sorry! we don't have this book yet :(")
        if book not in self.lendDict.keys():
            self.lendDict.update({book:user})
            self.bookslist.remove(book)
            print("Lender-Book database has been updated, you can take the book now")
        else:
            print(f"This book has already taken by {self.lendDict[book]}")

    def addBook(self, book):
        self.bookslist.append(book)
        print("The book has been added to the book-list, thank you for the contribution! :)")

    def returnBook(self, book):
        self.lendDict.pop(book)
        self.bookslist.append(book)

if __name__ == '__main__':
    const = Library(['Python', 'C', 'C++', 'Learn Java', 'JavaScript',
                     'DS and Algo'], "YourFreeLibrary")

    while(True):
        print(f"---Welcome to {const.name}---")
        print("Enter your choice to continue")
        ch1 = input("Press 1 to display the list of books\nPress 2 to lend a book\nPress 3 to donate a book\nPress 4 to return a book\n")
        if ch1 not in ['1', '2', '3', '4']:
            print("Please enter a valid choice!\n")
            continue
        ch = int(ch1)

        if ch == 1:
            const.displayBook()

        elif ch == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            const.lendBook(user, book)

        elif ch == 3:
            book = input("Enter the name of the book you want to donate: ")
            user = input("Enter your name: ")
            const.addBook(book)

        elif ch == 4:
            book = input("Enter the name of the book you want to return: ")
            user = input("Enter your name: ")
            const.returnBook(book)

        else:
            print("Please enter a valid choice")

        print("Enter 'Q' to quit and 'C' to continue")
        op = ""
        while(op != 'C' and op != 'Q'):
            option = input()
            op = option.capitalize()

            if op == 'Q':
                exit()

            elif op == 'C':
                continue

            else:
                print("Enter a valid choice")

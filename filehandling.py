import sqlite3
import os

# Create the table if it doesn't exist
def create_table():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books(
            book_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            description TEXT,
            pages INTEGER,
            curriculum TEXT        )
    ''')
    conn.commit()
    conn.close()

# Book class
class Book:
    def __init__(self, id, title, author, description, pages, curriculum, subject):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.pages = int(pages)
        self.curriculum = curriculum
        self.subject = subject
        # self.status = status

    def book_profile(self):
        print(f"\nBook Id: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\nDescription: {self.description}\nPages: {self.pages}\nStatus: {self.status.capitalize()}")

    def id_checker(self, book_id):
        return self.id == book_id

# Save book into the database
def insert_book(book):
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT OR REPLACE INTO books(book_id, title, author, description, pages, curriculum,subject)
        VALUES (?, ?, ?, ?, ?, ?,?)
    ''', (book.id, book.title, book.author, book.description, book.pages, book.curriculum, book.subject))
    conn.commit()
    conn.close()

# Library class to manage books
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)

    def book_search(self, book_id):
        for book in self.books:
            if book.id_checker(book_id):
                return book
        return None

    def books_availability(self):
        print("\nAvailable Books:")
        found = False
        for book in self.books:
            if book.status == "available":
                book.book_profile()
                found = True
        if not found:
            print("No available books.")

    def borrow(self):
        book_id = input("Please enter book ID to borrow: ").strip()
        book = self.book_search(book_id)
        if not book:
            print("Book not found.")
            return

        if book.status == "borrowed":
            print("Sorry, the book is already borrowed.")
            return

        confirm = input(f"Confirm borrowing '{book.title}'? Enter 'yes' to confirm: ").lower()
        if confirm == "yes":
            book.status = "borrowed"
            print(f"You have borrowed '{book.title}'.")
        else:
            print("Borrowing cancelled.")

    def operator(self):
        print("\nInput 1 to check book status")
        print("Input 2 to check available books")
        print("Input 3 to borrow a book")
        activity = input("Enter activity: ").strip()
        if activity == "1":
            book_id = input("Enter book ID: ").strip()
            book = self.book_search(book_id)
            if book:
                book.book_profile()
            else:
                print("Book not found.")
        elif activity == "2":
            self.books_availability()
        elif activity == "3":
            self.borrow()
        else:
            print("Enter a valid choice.")

# Main program
def main():
    create_table()
    library = Library()

    for i in range(3):
        print(f"\nEnter information for book number {i + 1}:")
        bk_id = input("Input book ID: ").strip()
        bk_title = input("Input book Title: ").strip()
        bk_author = input("Input book Author: ").strip()
        bk_description = input("Input book Description: ").strip()
        bk_pages = input("Input number of Pages: ").strip()
        bk_status = input("Input book Status (available/borrowed): ").strip().lower()
        bk_curriculum = input("Input book curriculum: ").strip()
        bk_subject = input("Input Book Subject e.g Business Studies: ").strip()

        book = Book(bk_id, bk_title, bk_author, bk_description, bk_pages, bk_curriculum, bk_subject)
        library.add_book(book)
        insert_book(book)

        # Save to text file
        with open('my_library.txt', 'a') as file:
            file.write(f"\nBook Id: {bk_id}\nTitle: {bk_title}\nAuthor: {bk_author}\nDescription: {bk_description}\nPages: {bk_pages}\nStatus: {bk_status}\n")

        print("Information has been saved.")

    print("\nAll Books in Library:")
    for book in library.books:
        book.book_profile()

    while True:
        library.operator()
        choice = input("\nTry another activity? 'y'/'n': ").lower()
        if choice != 'y':
            break

# Run main program
if __name__ == "__main__":
    main()
#  LEARN THIS 


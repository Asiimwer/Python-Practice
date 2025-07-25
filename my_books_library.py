import sqlite3
import os
from library_app import create_table
class Books():
    def __init__(self,id,title,author,description,subject,curriculum,b_class):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.subject = subject
        self.curriculum = curriculum
        self.bk_class = b_class

    def profile(self):
        profile = (f" \n Book ID : {self.id} \n Book Title : {self.title} \n Book Author : {self.author} \n Book Description : {self.description} \n Subject : {self.subject} \n Curriculum : {self.curriculum} \n Class : {self.bk_class} ")
        print(profile)

def save_book(books):
    conn = sqlite3.connect('my_library.db')
    cursor = conn.cursor()
    cursor.execute('''
                INSERT OR REPLACE INTO documents(book_id,book_title,book_author,book_description,book_subject,curriculum,book_class)
                VALUES(?,?,?,?,?,?,?) ''' , (books.id,books.title,books.author,books.description,books.subject,books.curriculum,books.bk_class))
    conn.commit()
    conn.close()
    print("Information saved to table books in 'my_library.db'")
print("Upload Content")
print()
print("Fill in the details to submit your resource")
while True :
    bk_id = input("Input book ID : ")
    while not bk_id.isdigit():
        print("Please Enter Integer e.g 01,02..")
        bk_id = input("Input book ID : ")
    bk_id = int(bk_id)
    bk_title = input("Enter Book title: ")
    bk_author = input("Enter Book author: ")
    bk_description = input("Enter Book description: ")
    bk_subject = input("Enter Subject e.g math: ")
    bk_curriculum = input("Enter Booksubject Curiculum (Cambrdge/UNEB) :")
    bk_class = input("Input Class e.g Yr : 13 : ")
    books = Books(bk_id,bk_title,bk_author,bk_description,bk_subject,bk_curriculum,bk_class)
    books.profile()
    save_book(books)
    proceed = input("Do you want to create another book ? (yes/yo) : ").strip()
    if proceed.lower() != "yes":
        break

class Book():
    def __init__(self,id,title,author,description,pages):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.pages = pages

    def book_profile(self):
        print(f" \n Book Id : {self.id}  \n Book Titile : {self.title} \n Book Author : {self.author} \n Book description : {self.description} \n Number pages : {self.pages} \n Status : {bk_status} ")
    def book_search(book_id):
            for book in books:
                if book.id_checker(book_id):
                    return book
            return None
class Library(Book):
        def __init__(self,id,title,author,description,pages,status):
            self.status = status
            super().__init__(id,title,author,description,pages)
        def id_checker(self,book_id):
            return self.id == book_id
        def books_availablity(self):
             print("Input 1 to see available books")
             print("Input 2 to see borrowed books")
             choice = int(input("Enter choice : "))
             if choice == 1:
                for book in books:
                  if bk_status.lower() == "available":
                      print(book)
             elif input == 2:
                 for book in books:
                  if bk_status.lower() == "borrowed":
                      print(book)
             else:
                 print("Enter correct Input")
        def borrow(self):
            print("Please enter book ID")
            book_idd = int(input("Book ID : "))
            # found = False
            if book_idd in books:
                bk_status = "borrowed"
                return bk_status

            while not book_id.isdigit():
                 print("Enter Integer")
                 book_id = input("Book ID : ")
            if book_id == self.id:
             confirm = input("Enter 'yes' to confirm and 'no' to cancel : ").lower()
             print(f" \n Book Id : {self.id} Book Titile : {self.title} \n Book Author : {self.author} \n Book description : {self.description} \n Number pages : {self.pages} Status : {self.status}")

            if confirm == 'yes':
                     self.status = "Borrowed"
            else:
                print("Please choose another book")  
        
        def operator(self):
            print(" \n Input 1 to check book status \n Input 2 for check for books availability \n Input 3 to borrow")
            activity = int(input("Enter activity : "))
            if activity == 1:
                book_id = input("Enter book Id")
                found = book_search(book_id)

            elif activity ==2:
                self.books_availablity()
            elif activity == 3:
                self.borrow()
            else:
                print("Enter valid code")
books = []
# bk_id = input("Input book ID :")
# while not bk_id.isdigit():
#     print("Please enter Integer")
while True:
    for i in range(3):
        print("\n")
        print(f"Enter infomation for book number {i+1}")
        bk_id = input("Input book ID :")
        bk_title= input("Input book Title : ")
        bk_author = input("Input book  Author : ")
        bk_description = input("Input book  Description : ")
        bk_pages = input("Input book  Pages : ")
        bk_status = input("Input book Status : ")
        book = Library(bk_id,bk_title,bk_author,bk_description,bk_pages,bk_status)
        new_book = books.append(book)
        with open('my_library.txt','a') as file:
            file.write(f" \n Book Id : {bk_id} Book Titile : {bk_title} \n Book Author : {bk_author} \n Book description : {bk_description} \n Number pages : {bk_pages} \n Status : {bk_status} ")
        print("Information has been saved")
    for book in books:
        book.book_profile()
    book.operator()
    choice = input("Try another activity ? 'y'/'n'")
    if choice.lower() != "y":
        break

        

        

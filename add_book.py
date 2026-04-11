from utils import books# import the books list from utils.py

def add():# define the add function
    book_name = input("Enter the Book name to add: ").upper()# get the book name from user and convert it to uppercase  
    books.append(book_name)# add the book name to the books list
    print(f"Book Added: {book_name}")# print the message with the added book name
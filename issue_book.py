from utils import books, issue_books# import the books and issue_books lists from utils.py

def issue():# define the issue function
    book_name = input("Enter book name: ").upper()# get the book name from user and convert it to uppercase
    if book_name in books:# check if the book is available
        books.remove(book_name)# remove the book from available books
        issue_books.append(book_name)# add the book to issued books
        print("Book assigned successfully")# print the message
    else:
        print("Book not available")# print the message
        
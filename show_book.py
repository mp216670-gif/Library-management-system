from utils import books# import the books list from utils.py
def show():# define the show function
    if len(books)==0:   print("Book not available")# check if there are no books available and print the message    
    else:# if there are books available
        for _ in books:# iterate through the books list and print each book name
            print(_)# print the book name
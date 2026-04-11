from add_book import add# import the add function from add_book.py
from issue_book import issue# import the issue function from issue_book.py
from show_book import show# import the show function from show_book.py
from return_book import return_book# import the return_book function from return_book.py

def library():# define the library function
    while True:# infinite loop to keep the program running until the user chooses to exit
        print("\n1. Add Book")# print the menu options
        print("2. Show Book")# print the menu options
        print("3. Issue Book")# print the menu options
        print("4. Return Book")# print the menu options
        print("5. Exit")# print the menu options
        choice = int(input("Enter your choice: "))# get the user's choice and convert it to an integer  
        
        if choice==1:   add()# call the add function if the user chooses option 1
        elif choice==2: show()# call the show function if the user chooses option 2
        elif choice==3: issue()# call the issue function if the user chooses option 3
        elif choice==4: return_book()# call the return_book function if the user chooses option 4   
        elif choice==5: # check if the user chooses option 5 to exit the program
            print("Thank you")# print a thank you message
            break# break the loop to exit the program
        else:# if the user enters an invalid choice
            print("Invalid choice")# print an error message
            
library()# call the library function to start the program
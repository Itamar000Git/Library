import hashlib
from tkinter import messagebox

import pandas as pd
import Book
import Serarch_strategy
from Book import BookFactory

'''
Observer class, have an update method that binding inheritance classes to implement.'''
class Observer:
    def update(self, subject):
        raise NotImplementedError("Subclasses must implement 'update' method.")

books_list = [] # List that contains al the books
librarian_list = [] #List that contains all users
available_list=[] #List that contains all available books
loaned_list=[] #List that contains all loaned books


'''
This class represent all librarian (users) abilities.
Contains init_library function that initial all files that need to initial.
 Also contains an option to add a user to the "users.cvs" file after created.'''
class Librarian(Observer):

    def __init__(self, name: str, age: int ,user_name: str, password: str):
        self.__name = name
        self.__age = age
        self.__user_name = user_name
        self.__is_librarian = True
        self.__password = password
        self.notification=[]

    #implementation of the observer method.
    def update(self, subject):
        self.notification.append(subject)
        print(f"{self.__name} have new notification.\n {subject}")

    def add_user(self):
        self.append("users.csv")

    #Generic function that append to a given file the user object (librarian) with the asked format.
    def append(self, filename: str):####add an new user
        pd.options.display.max_columns = None  # Show all columns
        pd.options.display.width = 0
        df = pd.read_csv(filename)
        new_row = {'name':self.get_name(), 'age':str(self.get_age()),'username':self.get_user_name(),'islibrarian':self.get_is_librarian(),'password':self.get_password()}
        new_row_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_row_df], ignore_index=True)
        df.to_csv(filename, index=False)


    #getters and setters
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_user_name(self):
        return str(self.__user_name)
    def get_is_librarian(self):
        return self.__is_librarian
    def get_password(self):
        return self.__password
    def __str__(self):
        return self.get_name() +' '+ str(self.get_age()) +' '+self.get_user_name()+ ' '+self.get_password()



    '''
    Initials all files that need to be init with the start values.
    This function use iterator for extraction the values from the csv files.
    '''
    @classmethod
    def init_library(cls):
        pd.options.display.max_columns = None
        pd.options.display.width = 0
        #clear_rows_from_csv('users.csv')######################################
        clear_rows_from_csv ('available_books.csv')
        clear_rows_from_csv('loaned_books.csv')

        with open('log.txt', 'a') as logger:
            logger.write("##############################system_open##################################\n")

        df=pd.read_csv("users.csv")
        print(df)
        for index, row in df.iterrows():
            new_user =[row['name'], row['age'], row['username'], row['password']]
            print(new_user)
            l1= Librarian(new_user[0], new_user[1], new_user[2], new_user[3])
            librarian_list.append(l1)

        df=pd.read_csv("books.csv")
        print(df)

        for index , row in df.iterrows(): #use iterator for extracting the needed information
            if row['waiting list'] != "[]" and row['waiting list'] != "NaN":
                waiting_list = str(row['waiting list']).split(',')
            else:
                waiting_list = ""
            #print(waiting_list.__str__())
            b1= Book.BookFactory.creat_book(row['title'], row['author'], row['is_loaned'], row['genre'], row['copies'],row['available'],waiting_list, row['year'])#############
            books_list.append(b1)

        for i in books_list: # sorted ava.csv and loaned.csv
            if i.get_is_loaned() == "Yes":
                loaned_list.append(i)
                #i.append("loaned_books.csv")
            elif i.get_is_loaned() == "No":
                available_list.append(i)
                #i.append("available_books.csv")
            else:
                print(f" something wrong: {i.__str__()}")
        # write_objects_to_csv(available_list,"available_books.csv")
        # write_objects_to_csv(loaned_list,"loaned_books.csv")
        update_files_from_list(available_list,"available_books.csv")
        update_files_from_list(loaned_list,"loaned_books.csv")

    #Function that creates user from list
    @classmethod
    def create_librarian(cls,new_user):
        librarian =Librarian(new_user[0],new_user[1],new_user[2],new_user[3])
        librarian_list.append(librarian)
        librarian.add_user()
        return librarian




#Function that check multiple exceptions using the value of "type" string.
def validate_input(a,type):
    if len(str(a)) == 0:
        raise ValueError("There are empty fields")
    elif not isinstance(a, int):
        raise ValueError(f"{type} input must be integers.")
    elif type == "age":
        if a < 0 or a>120:
            raise ValueError("Age must be between 0 and 120.")
    elif type == "copies":
        if a < 0:
            raise ValueError("Copies must be greater than zero.")
    elif type == "phone":
        if len(str(a)) != 9:
            raise ValueError("Phone number must be 10 digits and start with 0.")

#This function raise an exception if the field is empty.
def validate_non_empty_data(data):
    if not data:
        raise ValueError("Input cannot be empty")
    return data

#Function that use iterator to check if the given username already registered.
def check_user_name(user_name: str):
    for i in librarian_list:
        if i.get_user_name() == user_name:
            return True
    return False

#This function checks if a given hashed password match to the saved password in the user.csv file.
def check_password(user_input,user_ditailes):
    for i in librarian_list:
        if i.get_user_name() == user_ditailes:
            if i.get_password() == user_input:
                return True
            else:
                return False
        else:
            print(" something wrong")


'''
Add_book method implements the add book methodology.
The method use title search strategy, and implement it on the title of the new book that we want to add.
If we got results it's means that in the library may have this book (or maybe another book that starts with the same name).
For all results we check if one of them identical.
If this book have waiting list we let them know that we have available book.
'''
def add_book(book_dit_list):
    st=Serarch_strategy.search_book_title() #use title strategy
    optional_results=Serarch_strategy.search_book_title.search(st,book_dit_list[0] ,books_list,False)
    if len(optional_results)>0:
        for i in optional_results:
            if i.get_title() == book_dit_list[0]:
                #i.add_copies(book_dit_list[3])
                i.set_copies(i.get_copies()+book_dit_list[3])
                i.set_available_copies(i.get_available_copies()+book_dit_list[3])

                print("Book already exists , copy added")
                if len(i.get_waiting_list())>0 and i.get_waiting_list()[0]!= 'nan':
                    for j in range(i.get_available_copies()):
                        notify_lib(f"The book {i.get_title()} has available copy for {i.get_waiting_list()[0]}.")
                        print(i.get_waiting_list()[0])
                        i.remove_first()
                        print(i.get_waiting_list())
                        i.set_available_copies(i.get_available_copies()-1)
                if i.get_available_copies()>0:
                    i.set_is_loaned="No"
                    if not available_list.__contains__(i):
                        available_list.append(i)
                        loaned_list.remove(i)
                elif i.get_available_copies()==0:
                    i.set_is_loaned="Yes"
                    if i not in loaned_list:
                        available_list.remove(i)
                        loaned_list.append(i)

                update_files_from_list(books_list,"books.csv")

                with open('log.txt', 'a') as logger:
                    logger.write("book added successfully\n")
                return "exist"
    b1=BookFactory.creat_book(book_dit_list[0], book_dit_list[1],"No", book_dit_list[2], book_dit_list[3],book_dit_list[3],[], book_dit_list[4])#################
    print(f"New book added: {b1}")
    books_list.append(b1)
    available_list.append(b1)
    update_files_from_list(books_list,"books.csv")
    update_files_from_list(available_list,"available_books.csv")
    update_files_from_list(loaned_list,"loaned_books.csv")

    with open('log.txt', 'a') as logger:
        logger.write("book added successfully\n")
    return "new"

#This function implement the library observer with notifications that sent when a waited book is available.
def notify_lib(notify):
    for i in librarian_list:
        i.update(notify)
        print(i.notification)
    messagebox.showinfo("Notification", "All librarian got notification!")

#clear file if needed
def clear_rows_from_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.iloc[:0]
    df.to_csv(file_path, index=False)

#generic method that update a file from a given list.
def update_files_from_list(updated_list,file_name):
    pd.options.display.max_columns = None  # Show all columns
    pd.options.display.width = 0
    clear_rows_from_csv(file_name)
    for i in updated_list:
        i.append(file_name)


'''
"remove_book" function represent the remove operation.
When a librarian wants to eliminate a book from the library, first the method make sure that the book is exist.
After that we need to check if there is any loaned copy from this book.
For any "bad" option from above we raise an exception (in the call function).
If all the copies available The method remove the book from the book list and updating the files.'''
def remove_book(title):
    for i in books_list:
        if i.get_title() == title:
            if i.get_available_copies()==i.get_copies():
                books_list.remove(i)
                if available_list.__contains__(i):
                    available_list.remove(i)

                clear_rows_from_csv('available_books.csv')
                clear_rows_from_csv('books.csv')

                # write_objects_to_csv(available_list, "available_books.csv")
                # write_objects_to_csv(books_list, "books.csv")
                update_files_from_list(available_list, "available_books.csv")
                update_files_from_list(books_list, "books.csv")
                print("remove book")
                with open('log.txt', 'a') as logger:
                    logger.write("book removed successfully\n")
                return "found"
            else:
                with open('log.txt', 'a') as logger:
                    logger.write("book removed fail\n")
                return "loaned"
    print("book not found")
    with open('log.txt', 'a') as logger:
        logger.write("book removed fail\n")
    return "not found"


'''
"lend_book" function represent the lend methodology.
When a person wants to lend a book the system need to verify a few things first:
1. The book must be exist in the library, if not the borrowed fails.
2. The book must be available to loan (available copies in lib), Otherwise we need to save name and number for waiting list.
3. If there is a available book to loan, we loan it by decreasing the available copies.
    In that point we also have to check if this is the last book available and if it is, change the "is_loaned" field to "Yes".  
'''
def lend_book(title):
    from person_details_gui import get_person_details
    st=Serarch_strategy.search_book_title()
    optional_results=Serarch_strategy.search_book_title.search(st,title,books_list,False)
    for i in optional_results:
        if i.get_title() == title:
            i.set_popularity(i.get_popularity()+1)
            print(f"new popularity {i.get_popularity()} ")
            if i.get_available_copies() > 0:
                i.set_available_copies(i.get_available_copies()-1)
                if i.get_available_copies()==0:
                    i.set_is_loaned="Yes"
                    loaned_list.append(i)
                    available_list.remove(i)
                    update_files_from_list(loaned_list, "loaned_books.csv")
                    update_files_from_list(available_list, "available_books.csv")
                    update_files_from_list(books_list, "books.csv")
                    with open('log.txt', 'a') as logger:
                        logger.write("book borrowed successfully\n")
                    return "done"
                else:
                    # write_objects_to_csv(loaned_list, "loaned_books.csv")
                    # write_objects_to_csv(available_list, "available_books.csv")
                    # write_objects_to_csv(books_list, "books.csv")
                    update_files_from_list(books_list, "books.csv")
                    update_files_from_list(loaned_list, "loaned_books.csv")
                    update_files_from_list(available_list, "available_books.csv")
                    with open('log.txt', 'a') as logger:
                        logger.write("book borrowed successfully\n")
                    return "done"

            else:
                get_person_details(title)
                with open('log.txt', 'a') as logger:
                    logger.write("book borrowed fail\n")

                return "waiting list"

    with open('log.txt', 'a') as logger:
        logger.write("book borrowed fail\n")
    print("book not found")
    return "not found"

'''
The "return_book" function represent the return methodology.
When a person wants to return a book th system need to verify a few things first:
1. The book must be exist in the library, if not the return fails.
2. The system make sure that we dont reach to more available copies then actual copies.
3. When someone returns a book and the book doesn't have waiting list, we added 1 to the available copies.
   If before this return the book was unavailable so we also need to update "is_loaned" field to "No"
4. When that book have waiting list we just pass the book to the other person an short the list.
'''
def return_book(title):
    from person_details_gui import get_person_details
    st = Serarch_strategy.search_book_title()
    optional_results = Serarch_strategy.search_book_title.search(st, title, books_list, False)
    for i in optional_results:
        if i.get_title() == title:
            if i.get_available_copies()==i.get_copies():
                with open('log.txt', 'a') as logger:
                    logger.write("book returned fail\n")
                return "error"
            if i.get_available_copies() > 0 or len(i.get_waiting_list())==0 or i.get_waiting_list()[0]=='nan':
                i.set_available_copies(i.get_available_copies() + 1)
                if i not in available_list:
                    available_list.append(i)
                    loaned_list.remove(i)
                    i.set_is_loaned="No"


                with open('log.txt', 'a') as logger:
                    logger.write("book returned successfully\n")
                    update_files_from_list(loaned_list, "loaned_books.csv")
                    update_files_from_list(available_list, "available_books.csv")
                    update_files_from_list(books_list, "books.csv")

                return "done"
            elif i.get_available_copies() == 0 and i.get_waiting_list()[0]!='nan':
                notify_lib(f"The book {i.get_title()} has available copy for {i.get_waiting_list()[0]}.")
                i.remove_first()


                with open('log.txt', 'a') as logger:
                    logger.write("book returned successfully\n")
                update_files_from_list(loaned_list, "loaned_books.csv")
                update_files_from_list(available_list, "available_books.csv")
                update_files_from_list(books_list, "books.csv")

                return "loaned again"
    with open('log.txt', 'a') as logger:
        logger.write("book returned fail\n")
    print("book not found")
    return "book not found"

'''
This function sort the book list by their popularity field (highest first).
This filed updating in the constructor , the loan and the return methods. '''
def popular_books():
    copy_list=[]
    for i in books_list:
        copy_list.append(i)
    copy_list=sorted(copy_list,key=lambda book: book.get_popularity(),reverse=True)
    print("popular books")
    return copy_list



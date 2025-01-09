import hashlib
import pandas as pd
import Book
import Serarch_strategy
from Book import BookFactory

books_list = [] # List that contains al the books
librarian_list = [] #List that contains all users
available_list=[] #List that contains all available books
loaned_list=[] #List that contains all loaned books


'''
This class represent all librarian (users) abilities.
Contains init_library function that initial all files that need to initial.
 Also contains an option to add a user to the "users.cvs" file after created.'''
class Librarian:

    def __init__(self, name: str, age: int ,user_name: str, password: str):
        self.__name = name
        self.__age = age
        self.__user_name = user_name
        self.__is_librarian = True
        self.__password = password
        self.add_user()




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
        return self.get_name()+' '+str(self.get_age())+' '+self.get_user_name()+ ' '+self.get_password()



    '''
    Initials all files that need to be init with the start values.
    This function use iterator for extraction the values from the csv files.
    '''
    @classmethod
    def init_library(cls):
        pd.options.display.max_columns = None
        pd.options.display.width = 0
        clear_rows_from_csv('users.csv')######################################need to delete
        clear_rows_from_csv ('available_books.csv')
        clear_rows_from_csv('loaned_books.csv')


        def_user=["1",1,"1","1"] #################test user, can be deleted
        def_user[3]=hashlib.sha256(def_user[3].encode()).hexdigest()
        l1=Librarian.create_librarian(def_user)


        df=pd.read_csv("users.csv")
        print(df)
        df=pd.read_csv("books.csv")
        print(df)
        for index , row in df.iterrows(): #use iterator for extracting the needed information
            b1= Book.BookFactory.creat_book(row['title'], row['author'], row['is_loaned'], row['genre'], row['copies'], row['year'])
            books_list.append(b1)

        for i in books_list: # sorted ava.csv and loaned.csv
            if i.get_is_loaned() == "Yes":
                loaned_list.append(i)
                i.append("loaned_books.csv")
            elif i.get_is_loaned() == "No":
                available_list.append(i)
                i.append("available_books.csv")
            else:
                print(f" something wrong: {i.__str__()}")

    #Function that creates user from list
    @classmethod
    def create_librarian(cls,new_user):
        librarian =Librarian(new_user[0],new_user[1],new_user[2],new_user[3])
        librarian_list.append(librarian)
        print(librarian)
        return librarian


#Function that use iterator to check if the given username already registered.
def check_user_name(user_name: str):
    for i in librarian_list:
        if i.get_user_name() == user_name:
            return True
    return False

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

#This function raise an exception if the field is empty.
def validate_non_empty_data(data):
    if not data:
        raise ValueError("Input cannot be empty")
    return data


def add_book(book_dit_list):
    #check if it's a new book or old one
    st=Serarch_strategy.search_book_title()
    optional_results=Serarch_strategy.search_book_title.search(st,book_dit_list[0] ,books_list)
    if len(optional_results)>0:
        for i in optional_results:
            if i.get_title() == book_dit_list[0]:
                i.add_copies(book_dit_list[3])
                ##########################################################need to update copies
                print("Book already exists , copy added")
                if len(i.get_waiting_list())>0:###############################
                    print(i.get_waiting_list()[0])################################notification
                    i.get_waiting_list().remove(0)#########################
                update_files(i,"books.csv")################################
                if not available_list.__contains__(i):
                    available_list.append(i)
                    #update_files_from_list(available_list, "available_books.csv")
                return "exist"
    b1=BookFactory.creat_book(book_dit_list[0], book_dit_list[1],"No", book_dit_list[2], book_dit_list[3], book_dit_list[4])
    print(f"New book added: {b1}")
    books_list.append(b1)
    #b1.add_copies(b1.get_copies())
    b1.append("books.csv")
    return "new"
    # if len(optional_results)==0:
    #     b1=Book.BookFactory.creat_book(book_dit_list[0], book_dit_list[1],"No", book_dit_list[2], book_dit_list[3],book_dit_list[4])
    #     print(f"New book added: {b1}")
    #     return "new"
    #if new need to make new book

    #if old

def clear_rows_from_csv(file_path):
    df = pd.read_csv(file_path)
    df = df.iloc[:0]
    df.to_csv(file_path, index=False)

def update_files(book,filename):
    #book.append()###############################33
    df=pd.read_csv(str(filename))
    df.loc[df["title"]==book.get_title(),"copies"]=book.get_copies()
    df.to_csv("Books.csv",index=False)
    print(df)
    print("file updated")

def update_files_from_list(updated_list,file_name):
    pd.options.display.max_columns = None  # Show all columns
    pd.options.display.width = 0
    clear_rows_from_csv(file_name)
    for i in updated_list:
        i.append(file_name)
    df = pd.read_csv(file_name)
    print(f"####################################{file_name}###################################################")
    print(df)


def remove_book(title):
    for i in books_list:
        if i.get_title() == title:
            if i.get_available_copies()==i.get_copies():
                books_list.remove(i)
                if available_list.__contains__(i):
                    available_list.remove(i)

                clear_rows_from_csv('available_books.csv')
                clear_rows_from_csv('books.csv')
                update_files_from_list(available_list, "available_books.csv")
                update_files_from_list(books_list, "books.csv")
                print("remove book")
                return "found"
            else:
                return "loaned"
    print("book not found")
    return "not found"



def lend_book():
    print("lend book")

def return_book():
    print("return book")

def popular_books():
    copy_list=[]
    for i in books_list:
        copy_list.append(i)
    copy_list=sorted(copy_list,key=lambda book: book.get_popularity(),reverse=True)################################
    print("popular books")
    return copy_list
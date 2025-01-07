import hashlib
import csv
import pandas as pd
import Book



class Person:
    def __init__(self, name: str, age: int ):
        self.__name = name
        self.__age = age
        self.__is_librarian = False


    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age


class Customer(Person):
    def __init__(self, name: str, age: int ,user_name: str):
        super().__init__(name, age)
        self.__user_name = user_name
        ###need to make sure that is labrarian == FALSE###

    def get_user_name(self):
        return self.__user_name
    def get_is_librarian(self):
        return self.__is_librarian
    def __str__(self):
        return self.get_name()+' '+str(self.get_age())+' '+self.get_user_name()



    ######need to implement password#####

class Librarian(Person):
    books_list = []
    def __init__(self, name: str, age: int ,user_name: str, password: str):
        super().__init__(name, age)
        self.__user_name = user_name
        self.__is_librarian = True
        self.__password = hashlib.sha256(password.encode()).hexdigest()#############33
        self.add_user()########################

    # def search_book_title(self, text):
    # # need to fine all books that there title starts with text
    # def search_book_auther(self, text):
    # #need to fine all books that there title starts with text
    # def search_book_year(self, text):
    # # need to fine all books that there title starts with text
    # def search_book_genre(self, text):
    # # need to fine all books that there title starts with text

    #def add_book(self,num_of_copies):
        ####if exist add copies if not create new book


    def add_user(self):##############################
        self.appand("users.csv")###########################

    def appand(self, filename: str):####add an new user
        pd.options.display.max_columns = None  # Show all columns###############################
        pd.options.display.width = 0  #############################
        df = pd.read_csv(filename)
        new_row = {'name':self.get_name(), 'age':str(self.get_age()),'username':self.get_user_name(),'islibrarian':self.get_is_librarian(),'password':self.get_password()}
        new_row_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_row_df], ignore_index=True)
        df.to_csv(filename, index=False)














    def get_user_name(self):
        return self.__user_name
    def get_is_librarian(self):
        return self.__is_librarian
    def get_password(self):
        return self.__password
    def __str__(self):
        return self.get_name()+' '+str(self.get_age())+' '+self.get_user_name()+ ' '+self.get_password()












    @classmethod
    def clear_rows_from_csv(cls,file_path):  ##########################
        df = pd.read_csv(file_path)
        df = df.iloc[:0]
        df.to_csv(file_path, index=False)

    #def search_book(text):
    @classmethod
    def init_library(cls):  ####################################################33
        pd.options.display.max_columns = None  # Show all columns###############################
        pd.options.display.width = 0  #############################
        cls.clear_rows_from_csv('users.csv')  ####################
        cls.clear_rows_from_csv ('available_books.csv')
        cls.clear_rows_from_csv('loaned_books.csv')


        c1= Librarian("Dan",26,"Dan12","1234")####################################
        c2 =Librarian("Moshe",35,"MoshMosh","4321")####################################

        df=pd.read_csv("users.csv")
        print(df)

        df=pd.read_csv("Books.csv")##################################

        for index , row in df.iterrows():######################################
            #print(row)
            b1= Book.BookFactory.creat_book(row['title'], row['author'], row['is_loaned'], row['genre'], row['copies'], row['year'])
            print(f"{index}:{b1}")
            cls.books_list.append(b1)

        for i in cls.books_list: # sorted ava.csv and loaned.csv#########################################333
            if i.get_is_loaned() == "No":
                i.appand("loaned_books.csv")
            elif i.get_is_loaned() == "Yes":
                i.appand("available_books.csv")
            else:
                print(f" somthig wrong: {i.__str__()}")





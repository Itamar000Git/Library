from abc import ABC ,abstractmethod
from typing import Optional
import pandas as pd
'''Book class: represent book in the library with all the essential fields.
    important fields:
    available_copies: represent number of available books, updated with add a book (that exist or new one) and from return book.
    popularity: represent the popularity of each book. Actually its a number of requested to loaned.
    waiting_list: a list of strings that represent number of peoples  that ask for a book that dont have available book. '''
class Book(ABC):
    def __init__(self, title: str, author: str,is_loaned: str,genre : str, copies: int,available: int,waiting_list:list,year: int): ##########################
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__copies = copies
        self.__year = year
        self.__is_loaned = is_loaned
        self.__available_copies = available
        if waiting_list[0] != 'nan':
            self.__popularity =(copies - available) + waiting_list.__len__()
        else:
            self.__popularity = (copies - available)
        self.__waiting_list=waiting_list



    def remove_first(self):
        self.__waiting_list.remove(self.__waiting_list[0])

    # def request_to_loan(self):
    #     if self.__available_copies >= 1:
    #         self.__available_copies=self.__available_copies-1
    #     else:
    #         print("No available copies")
    #         return False

    # #function that added copies and updated available field
    # def add_copies(self,num_of_copies):#just a new book copy not returned one
    #     #maybe need to take in consider a new book
    #     self.__copies=  self.__copies+num_of_copies
    #     self.__available_copies= self.__available_copies+num_of_copies
    #     print(f"Added {num_of_copies} copies of {self.__title}")




        # df=pd.read_csv("books.csv")
        # df.loc[df["title"]==self.get_title(),"copies"]=
        # df.to_csv("Books.csv",index=False)
        # print(df)
        #############################log############
    #Generic function that append an object to a given file. the object should support file fields.
    def append(self, filename: str):#add a book to some file (ava.csv or loaned.csv)
        pd.options.display.max_columns = None  # Show all columns
        pd.options.display.width = 0
        df = pd.read_csv(filename)
        if self.get_waiting_list().__str__() == "['nan']" or self.get_waiting_list().__str__() == "NaN" : #####################
            new_row = {'title': self.get_title(), 'author': str(self.get_author()), 'is_loaned': self.get_is_loaned(),
                       'copies': self.get_copies(), 'available': self.get_available_copies(),
                       'waiting list': None, 'genre': self.get_genre(), 'year': self.get_year()}
        else:
            new_row = {'title':self.get_title(), 'author':str(self.get_author()),'is_loaned':self.get_is_loaned(),'copies':self.get_copies(),'available':self.get_available_copies(),'waiting list':self.get_waiting_list(),'genre':self.get_genre(),'year':self.get_year()}

        new_row_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_row_df], ignore_index=True)
        df.to_csv(filename, index=False)


    #Generic function that get object, text and string, the function checks if text is part of the one of the fields in the object.
    #The field that need to check with being chosen by the "search_by" string.
    def startswith(self,text,search_by):
        if len(text)==0:
            print("No search term")
            return False
        if search_by == "title":
            if len(text)>len(self.__title):
                return False
            for i in range(len(text)) :
                if text[i]!=self.__title[i]:
                    return False
            return True
        elif search_by == "author":
            if len(text)>len(self.__author):
                return False
            for i in range(len(text)) :
                if text[i]!=self.__author[i]:
                    return False
            return True
        elif search_by == "genre":
            if len(text)>len(self.__genre):
                return False
            for i in range(len(text)) :
                if text[i]!=self.__genre[i]:
                    return False
            return True
        elif search_by == "year":
            if len(str(text))>len(str(self.__year)):
                return False
            for i in range(len(text)) :
                if str(text)[i]!=str(self.__year)[i]:
                    return False
            return True
        else:
            print("Invalid search term")
            return "error"

    #getters&setters
    def get_loaned(self):
        return self.__copies - self.__available_copies
    def get_is_loaned(self):
        return self.__is_loaned
    def get_title(self) -> str:
        return self.__title
    def get_author(self) -> str:
        return self.__author
    def get_genre(self) -> str:
        return self.__genre
    def get_copies(self) -> int:
        return self.__copies
    def get_year(self) -> int:
        return self.__year
    def get_available_copies(self) -> int:
        return self.__available_copies
    def get_waiting_list(self) -> list:
        return self.__waiting_list
    def get_popularity(self) -> int:
        return self.__popularity


    def set_is_loaned(self,value):##################
        self.__is_loaned = value
    def set_popularity(self,popularity):
        self.__popularity=popularity
    def set_available_copies(self,available_copies):
        self.__available_copies=available_copies
    def set_copies(self, copies):
        self.__copies=copies

    def __str__(self):
        return self.__title + ' ' + self.__author + ' ' + self.__genre + ' ' + str(self.__copies) + ' '+str(self.__available_copies)+' '+self.__waiting_list.__str__() +''+ str(self.__year)







#class for each genre to implement factory.
class Fiction (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Fiction",copies,available,waiting_list,year)

class Dystopian (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Dystopian",copies,available,waiting_list,year)

class Classic (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Classic",copies,available,waiting_list,year)

class Adventure (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Adventure",copies,available,waiting_list,year)

class Romance (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Romance",copies,available,waiting_list,year)

class HistoricalFiction (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Historical Fiction",copies,available,waiting_list,year)

class PsychologicalDrama (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Psychological Drama",copies,available,waiting_list,year)

class Philosophy (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Philosophy",copies,available,waiting_list,year)

class EpicPoetry (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Epic Poetry",copies,available,waiting_list,year)

class GothicFiction (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Gothic Fiction",copies,available,waiting_list,year)

class GothicRomance (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Gothic Romance",copies,available,waiting_list,year)

class Realism (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str, copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Realism",copies,available,waiting_list,year)

class Modernism (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Modernism",copies,available,waiting_list,year)

class Satire (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Satire",copies,available,waiting_list,year)

class ScienceFiction (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Science Fiction",copies,available,waiting_list,year)

class Tragedy (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Tragedy",copies,available,waiting_list,year)

class Fantasy (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,available: int,waiting_list:list,year: int):
        super().__init__(title, author,is_loaned,"Fantasy",copies,available,waiting_list,year)


#factory implementation by genre. support the option to add a book with new genre.
class BookFactory:
    @staticmethod
    def creat_book(title: str, author: str, is_loaned: str, genre:str ,copies: int,available:int,waiting_list:list,year: int)-> Optional[Book]:
        if copies < 0 :
            print("Error: number of duplicates cannot be negative")
            return None
        if genre == "Fiction":
            return Fiction(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Dystopian":
            return Dystopian(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Classic":
            return Classic(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Adventure":
            return Adventure(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Romance":
            return Romance(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Historical Fiction":
            return HistoricalFiction(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Psychological Drama":
            return PsychologicalDrama(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Philosophy":
            return Philosophy(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "EpicPoetry":
            return EpicPoetry(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Gothic Fiction":
            return GothicFiction(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Gothic Romance":
            return GothicRomance(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Realism":
            return Realism(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Modernism":
            return Modernism(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Tragedy":
            return Tragedy(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Fantasy":
            return Fantasy(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Epic Poetry":
            return EpicPoetry(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Satire":
            return Satire(title, author,is_loaned, copies,available,waiting_list, year)
        elif genre == "Science Fiction":
            return ScienceFiction(title, author,is_loaned, copies,available,waiting_list, year)
        else:
            return Book(title, author,is_loaned,genre, copies,available,waiting_list, year)

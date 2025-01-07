from abc import ABC ,abstractmethod
from typing import Optional
import pandas as pd

class Book(ABC):
    def __init__(self, title: str, author: str,is_loaned: str,genre : str, copies: int,year: int): ##########################
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__copies = copies
        self.__year = year
        self.__is_loaned = is_loaned
        self.__available_copies=self.__copies
        self.__dic_copies={}
        for i in range(copies):
            self.__dic_copies[i]=True#need to update according to books.csv

    def request_to_loan(self):
        if self.__available_copies >= 1:
            self.__available_copies=self.__available_copies-1
            for i in self.__dic_copies: #####################################
                if self.__dic_copies[i]==True:
                    self.__dic_copies[i]=False
                    return True
        else:
            print("No available copies")
            return False

    def add_copies(self,num_of_copies):#just a new book copy not returned one
        #maybe need to take in consider a new book
        self.__copies+=num_of_copies
        self.__available_copies= self.__available_copies+num_of_copies
        self.__dic_copies[self.__copies]=True
        print(f"Added {num_of_copies} copies of {self.__title}")
        # df=pd.read_csv("books.csv")
        # df.loc[df["title"]=="The Catcher in the Rye","copies"]="5"
        # df.to_csv("Books.csv",index=False)
        # print(df)
        #############################log############

    def appand(self, filename: str): ################### add a book to some file (ava.csv or loaned.csv)
        pd.options.display.max_columns = None  # Show all columns###############################
        pd.options.display.width = 0  #############################
        df = pd.read_csv(filename)
        new_row = {'title':self.get_title(), 'author':str(self.get_author()),'is_loaned':self.get_is_loaned(),'copies':self.get_copies(),'genre':self.get_genre(),'year':self.get_year()}
        new_row_df = pd.DataFrame([new_row])
        df = pd.concat([df, new_row_df], ignore_index=True)
        df.to_csv(filename, index=False)

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
    def get_dic_copies(self) -> dict:
        return self.__dic_copies

    def __str__(self):
        return self.__title + ' ' + self.__author + ' ' + self.__genre + ' ' + str(self.__copies) + ' ' + str(self.__year)







############prbpably wrong
class Fiction (Book, ABC) :#####################################
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Fiction",copies,year)

class Dystopian (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,year: int):
        super().__init__(title, author,is_loaned,"Dystopian",copies,year)

class Classic (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Classic",copies,year)

class Adventure (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Adventure",copies,year)

class Romance (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Romance",copies,year)

class HistoricalFiction (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Historical Fiction",copies,year)

class PsychologicalDrama (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Psychological Drama",copies,year)

class Philosophy (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Philosophy",copies,year)

class EpicPoetry (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,year: int):
        super().__init__(title, author,is_loaned,"Epic Poetry",copies,year)

class GothicFiction (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Gothic Fiction",copies,year)

class GothicRomance (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str , copies: int,year: int):
        super().__init__(title, author,is_loaned,"Gothic Romance",copies,year)

class Realism (Book, ABC) :
    def __init__(self, title: str, author: str,is_loaned:str, copies: int,year: int):
        super().__init__(title, author,is_loaned,"Realism",copies,year)

class Modernism (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,year: int):
        super().__init__(title, author,is_loaned,"Modernism",copies,year)

class Satire (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,year: int):
        super().__init__(title, author,is_loaned,"Satire",copies,year)

class ScienceFiction (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,year: int):
        super().__init__(title, author,is_loaned,"Science Fiction",copies,year)

class Tragedy (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,year: int):
        super().__init__(title, author,is_loaned,"Tragedy",copies,year)

class Fantasy (Book, ABC) :
    def __init__(self, title: str, author: str, is_loaned:str ,copies: int,year: int):
        super().__init__(title, author,is_loaned,"Fantasy",copies,year)

class BookFactory:
    @staticmethod
    def creat_book(title: str, author: str, is_loaned: str, genre:str ,copies: int,year: int)-> Optional[Book]: #################
        if copies < 0 :
            print("Error: number of duplicates cannot be negative")
            return None
        if genre == "Fiction":
            return Fiction(title, author,is_loaned, copies, year)
        elif genre == "Dystopian":
            return Dystopian(title, author,is_loaned, copies, year)
        elif genre == "Classic":
            return Classic(title, author,is_loaned, copies, year)
        elif genre == "Adventure":
            return Adventure(title, author,is_loaned, copies, year)
        elif genre == "Romance":
            return Romance(title, author,is_loaned, copies, year)
        elif genre == "Historical Fiction":
            return HistoricalFiction(title, author,is_loaned, copies, year)
        elif genre == "Psychological Drama":
            return PsychologicalDrama(title, author,is_loaned, copies, year)
        elif genre == "Philosophy":
            return Philosophy(title, author,is_loaned, copies, year)
        elif genre == "EpicPoetry":
            return EpicPoetry(title, author,is_loaned, copies, year)
        elif genre == "Gothic Fiction":
            return GothicFiction(title, author,is_loaned, copies, year)
        elif genre == "Gothic Romance":
            return GothicRomance(title, author,is_loaned, copies, year)
        elif genre == "Realism":
            return Realism(title, author,is_loaned, copies, year)
        elif genre == "Modernism":
            return Modernism(title, author,is_loaned, copies, year)
        elif genre == "ScienceFiction":
            return ScienceFiction(title, author,is_loaned, copies, year)
        elif genre == "Tragedy":
            return Tragedy(title, author,is_loaned, copies, year)
        elif genre == "Fantasy":
            return Fantasy(title, author,is_loaned, copies, year)
        elif genre == "Epic Poetry":
            return EpicPoetry(title, author,is_loaned, copies, year)
        elif genre == "Satire":
            return Satire(title, author,is_loaned, copies, year)#######################
        elif genre == "Science Fiction":
            return ScienceFiction(title, author,is_loaned, copies, year)#####################3


#def main():

    # b1= BookFactory.creat_book("The Hobbit","J.R.R. Tolkien","Fantasy",4,1937)
    # print(b1)



# if __name__ == "__main__":
#     main()
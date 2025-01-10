from abc import ABC ,abstractmethod

from Librarian import*####################################################
class SearchStrategy(ABC):
    @abstractmethod
    def search(self,text,books_list):
        pass

optional_results=[]
class search_book_title(SearchStrategy):
    def search(self,text,books_list):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(text,"title")]


        return optional_results

class search_book_author(SearchStrategy):
    def search(self,text,books_list):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(text,"author")]

        return optional_results

class search_book_genre(SearchStrategy):
    def search(self,text,books_list):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(text,"genre")]
        return optional_results

class search_book_year(SearchStrategy):
    def search(self,text_int,books_list):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(str(text_int),"year")]
        return optional_results



# need to fine all books that there title starts with text
# def search_book_auther(self, text):
#     #need to fine all books that there title starts with text
# def search_book_year(self, text):
#     # need to fine all books that there title starts with text
# def search_book_genre(self, text):
#     # need to fine all books that there title starts with text
# def add_book(self,num_of_copies):
#     ###if exist add copies if not create new book

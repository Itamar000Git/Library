from abc import ABC ,abstractmethod

from Librarian import*####################################################
class SearchStrategy(ABC):
    @abstractmethod
    def search(self,text,books_list,log):
        pass

optional_results=[]
class search_book_title(SearchStrategy):
    def search(self,text,books_list,log):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(text,"title")]
        if log:
            if len(optional_results) > 0:  ############################################################################
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by name completed successfully\n")
            else:
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by name fail\n")



        return optional_results

class search_book_author(SearchStrategy):
    def search(self,text,books_list,log):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(text,"author")]
        if log:
            if len(optional_results) > 0:  ############################################################################
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by author completed successfully\n")
            else:
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by author fail\n")

        return optional_results

class search_book_genre(SearchStrategy):
    def search(self,text,books_list,log):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(text,"genre")]

        if log:
            if len(optional_results) > 0:  ############################################################################
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by genre completed successfully\n")
            else:
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by genre fail\n")

        return optional_results

class search_book_year(SearchStrategy):
    def search(self,text_int,books_list,log):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(str(text_int),"year")]

        if log:
            if len(optional_results) > 0:  ############################################################################
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text_int} by year completed successfully\n")
            else:
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text_int} by year fail\n")

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

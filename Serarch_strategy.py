from abc import ABC ,abstractmethod

from Librarian import*
class SearchStrategy(ABC):
    """
    The SearchStrategy class serves as an abstract base class for various book search strategies.
    Subclasses must implement the 'search' method, defining how the search is performed.
    This class is part of the Strategy design pattern to allow flexible and extendable search functionalities.
    """

    @abstractmethod
    def search(self,text,books_list,log):
        pass

optional_results=[]
class search_book_title(SearchStrategy):
    """
    Implements the search strategy for finding books by their title.
    Logs the search operation's success or failure if logging is enabled.
    """
    def search(self,text,books_list,log):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(text,"title")]
        if log:
            if len(optional_results) > 0:
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by name completed successfully\n")
            else:
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by name fail\n")



        return optional_results

class search_book_author(SearchStrategy):
    """
    Implements the search strategy for finding books by their author.
    Logs the search operation's success or failure if logging is enabled.
    """
    def search(self,text,books_list,log):
        global optional_results
        optional_results = [s for s in books_list if s.startswith(text,"author")]
        if log:
            if len(optional_results) > 0:
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by author completed successfully\n")
            else:
                with open('log.txt', 'a') as logger:
                    logger.write(f"Search book {text} by author fail\n")

        return optional_results

class search_book_genre(SearchStrategy):
    """
    Implements the search strategy for finding books by their genre.
    Logs the search operation's success or failure if logging is enabled.
    """
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
    """
    Implements the search strategy for finding books by their year.
    Logs the search operation's success or failure if logging is enabled.
    """
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


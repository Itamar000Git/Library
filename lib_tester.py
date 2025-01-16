import time
import unittest

import Librarian
import Serarch_strategy
import person_details_gui

from Librarian import *
from Book import BookFactory

class MyTestCase(unittest.TestCase):
###Please don't run all tests together!
    '''
    Checks if the system can identify duplicate usernames.
    Creates two users with the same username and ensures the system detects the conflict.
    '''
    def test_duplicated_user_name(self):
        c1 =["Dan", 26, "the_same", "1234"]
        Librarian.create_librarian(c1)
        c2 = ["ben", 30, "the_same", "1111"]
        self.assertTrue(check_user_name(c2[2]))

    '''
    Verifies that the system raises errors for invalid age inputs.
    Tests with a non-numeric age and a negative age.
    '''
    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            c2 = ["ben", "aa", "the_same", "1111"]
            validate_input(c2[1],"age")
        with self.assertRaises(ValueError):
            c1 = ["Dan", -1, "dan12", "1234"]
            validate_input(c1[1],"age")


    '''
    Tests password hashing and validation functionality.
    Hashes passwords for two librarians and checks if the passwords match correctly.
    '''
    def test_cradential(self):
        c1 =["Dan", 26, "Dan12", "1234"]
        c2 = ["ben", 10, "ben21", "1111"]
        c1[3] = hashlib.sha256(c1[3].encode()).hexdigest()
        c2[3] = hashlib.sha256(c2[3].encode()).hexdigest()

        l1=Librarian.create_librarian(c1)
        l2=Librarian.create_librarian(c2)
        self.assertTrue( check_password(l1.get_password(),"Dan12"))

        self.assertFalse(check_password(l2.get_password(),"Dan12"))
        self.assertTrue(check_password(l2.get_password(), "ben21"))



    '''
    Tests the removal of books based on their status (loaned, available, or non-existent).
    Attempts to remove books in various scenarios and checks the responses.
    '''

    def test_removed_loaned_book(self):
        new_b = ["test", "myself", "Fantasy", 2, 2005]
        Librarian.init_library()
        result=remove_book("1984")
        self.assertTrue(result=="loaned")


        add_book(new_b)
        result=remove_book("test")
        self.assertTrue(result=="found")

        result=remove_book("not exist book")
        self.assertTrue(result=="not found")





    '''
    Checks the system's behavior when attempting to loan a non-existent book.
    Ensures the system returns the correct response.
    '''
    def test_loaned_not_exist_book(self):
        b = lend_book("not exist book")
        self.assertTrue(b=="not found")


    '''
   Tests the system's handling of books with limited availability.
   Loans a book until no copies are left and ensures the response transitions to a waiting list.
    '''
    def test_loaned_unavailable_book(self):
        new_b = ["test1", "myself", "other", 2, 2005]
        Librarian.init_library()
        add_book(new_b)
        b=lend_book("test1")
        self.assertTrue(b == "done")
        b=lend_book("test1")
        self.assertTrue(b == "done")
        b=lend_book("test1")
        self.assertTrue(b == "waiting list")

        return_book("test1")
        return_book("test1")
        remove_book("test1")



    '''
    Tests adding new books and updating copies of existing books.
    Adds a new book, removes it, re-adds it, and checks if the copies are updated correctly.
    '''
    def test_add_new_or_exist(self):

        Librarian.init_library()

        new_b=BookFactory.creat_book("test2", "myself","No", "other", 2,2,[], 2005)
        new_b_dit=[new_b.get_title(),new_b.get_author(),new_b.get_genre(),new_b.get_copies(),new_b.get_year()]
        add_book(new_b_dit)
        self.assertTrue( new_b in books_list)
        remove_book("test2")
        self.assertTrue(new_b not in books_list)

        new_b = BookFactory.creat_book("test2", "myself", "No", "other", 2, 2, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit)
        self.assertEqual(new_b.get_copies(), 2)

        self.assertTrue(new_b in books_list)
        add_book(new_b_dit)
        for i in books_list:
            if i.get_title() == new_b.get_title():
                self.assertEqual(i.get_copies(), 4)
                break
        remove_book("test2")





        '''
       Checks the behavior of adding books when a waiting list exists.
       Adds a book with limited copies, handles waiting list entries, and verifies updates after returning books.
       '''
    def test_add_book_with_waiting_list(self):
        Librarian.init_library()
        new_b=BookFactory.creat_book("test3", "myself","No", "other", 1,0,[], 2005)
        new_b_dit=[new_b.get_title(),new_b.get_author(),new_b.get_genre(),new_b.get_copies(),new_b.get_year()]
        add_book(new_b_dit)
        lend_book("test3")
        for i in books_list:
            if i.get_title() == new_b.get_title():
                i.get_waiting_list().append({'aaaaa': '0545870209'})


        new_b = BookFactory.creat_book("test3", "myself", "No", "other", 1, 1, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit)

        for i in books_list:
            if i.get_title() == new_b.get_title():
                self.assertEqual(i.get_copies(),2)
                self.assertEqual(i.get_available_copies(), 0)

        return_book("test3")
        return_book("test3")
        remove_book("test3")


    '''
       Ensures correct search results when looking for books by title.
       Searches for a non-existent book, adds it, and verifies it appears in the results.
       '''

    def test_search_new_book(self):
        Librarian.init_library()

        stra=Serarch_strategy.search_book_title()
        results=stra.search("test4",books_list,True)
        self.assertTrue(len(results)==0)

        new_b=BookFactory.creat_book("test4", "myself","No", "other", 1,1,[], 2005)
        new_b_dit=[new_b.get_title(),new_b.get_author(),new_b.get_genre(),new_b.get_copies(),new_b.get_year()]
        add_book(new_b_dit)

        results=stra.search("test4",books_list,True)

        self.assertTrue(new_b in results)

        remove_book("test4")


    def test_search_results(self):
        Librarian.init_library()
        new_b1=BookFactory.creat_book("test1", "myself","No", "other", 1,1,[], 2005)
        new_b_dit1=[new_b1.get_title(),new_b1.get_author(),new_b1.get_genre(),new_b1.get_copies(),new_b1.get_year()]
        add_book(new_b_dit1)
        new_b2=BookFactory.creat_book("test2", "myself","No", "other", 1,1,[], 2005)
        new_b_dit2=[new_b2.get_title(),new_b2.get_author(),new_b2.get_genre(),new_b2.get_copies(),new_b2.get_year()]
        add_book(new_b_dit2)
        new_b3=BookFactory.creat_book("test3", "myself","No", "other", 1,1,[], 2005)
        new_b_dit3=[new_b3.get_title(),new_b3.get_author(),new_b3.get_genre(),new_b3.get_copies(),new_b3.get_year()]
        add_book(new_b_dit3)
        new_b4=BookFactory.creat_book("test4", "myself","No", "other", 1,1,[], 2005)
        new_b_dit4=[new_b4.get_title(),new_b4.get_author(),new_b4.get_genre(),new_b4.get_copies(),new_b4.get_year()]
        add_book(new_b_dit4)

        stra = Serarch_strategy.search_book_title()
        results = stra.search("test", books_list,True)
        self.assertTrue(len(results)==4)
        self.assertTrue(new_b1 in results)
        self.assertTrue(new_b2 in results)
        self.assertTrue(new_b3 in results)
        self.assertTrue(new_b4 in results)

        remove_book("test1")
        remove_book("test2")
        remove_book("test3")
        remove_book("test4")

    '''
    This test verifies the most popular book in the library based on borrowing activity.
    It checks that the popularity of a book changes after multiple borrowings, and ensures the book 
    remains the most popular until the new book is borrowed enough times.
    '''
    def test_popularity_result(self):
        Librarian.init_library()
        popular=popular_books()
        print(popular[0].get_title())
        self.assertTrue(popular[0].get_title() == "1984")
        new_b = BookFactory.creat_book("test5", "myself", "No", "other", 10, 10, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit)

        for i in range(5):
            lend_book("test5")
        popular = popular_books()

        self.assertTrue(popular[0].get_title() == "1984")
        lend_book("test5")
        popular = popular_books()

        self.assertTrue(popular[0].get_title() == "test5")

        for i in range(6):
            return_book("test5")

        remove_book("test5")

        '''
           This test checks the behavior of a book that has only one available copy.
           It ensures that when the book is borrowed, it gets moved to the loaned list,
           and is removed from the available list until it is returned.
           '''

    def test_loaned_last_ava_book(self):
        Librarian.init_library()
        new_b = BookFactory.creat_book("test6", "myself", "No", "other", 1, 1, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit)
        self.assertTrue(new_b in books_list)
        self.assertTrue(new_b in available_list)
        self.assertTrue(new_b not in loaned_list)
        lend_book("test6")

        self.assertTrue(new_b not in available_list)
        self.assertTrue(new_b in loaned_list)

        return_book("test6")
        remove_book("test6")


    '''
    This test ensures that the system raises the correct exceptions (ValueError) when invalid data is input.
    It checks for various invalid inputs such as empty strings, negative numbers, and invalid phone numbers.
    '''

    def test_exceptions_raises(self):
        Librarian.init_library()
        self.assertRaises(ValueError, validate_non_empty_data,"")

        self.assertRaises(ValueError,validate_input,"","non")
        self.assertRaises(ValueError, validate_input, "a", "non")
        self.assertRaises(ValueError, validate_input, -5, "age")
        self.assertRaises(ValueError, validate_input, -5, "copies")
        self.assertRaises(ValueError, validate_input, 11111, "phone")


    '''
    This test verifies that the system logs all important actions, such as adding, removing, 
    and searching for books. It checks that each action is correctly logged to a file, and then 
    verifies the content of the log file against the expected log entries
    '''

    def test_log(self):

        with open('log.txt', 'w') as logger:
            pass  # Opening in write mode clears the file
        logger=[]
        log_txt=[]

        Librarian.init_library() ##############################system_open##################################
        logger.append("##############################system_open##################################")
        new_b = BookFactory.creat_book("test7", "myself", "No", "other", 1, 1, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit) ###book added successfully
        logger.append("book added successfully")
        add_book(new_b_dit) ###book added successfully
        logger.append("book added successfully")
        #book added fail happened in typing error

        remove_book("test7")#book removed successfully
        logger.append("book removed successfully")
        remove_book("test7")#book removed fail
        logger.append("book removed fail")

        title_stra=Serarch_strategy.search_book_title()
        author_stra=Serarch_strategy.search_book_author()
        genre_stra=Serarch_strategy.search_book_genre()
        year_stra=Serarch_strategy.search_book_year()

        filter_list=title_stra.search("test8",books_list,True)#Search book test8 by name fail
        logger.append("Search book test8 by name fail")
        filter_list=author_stra.search("myself",books_list,True)#Search book myself by author fail
        logger.append("Search book myself by author fail")
        filter_list=genre_stra.search("other",books_list,True)#Search book other by genre fail
        logger.append("Search book other by genre fail")
        filter_list=year_stra.search("2005",books_list,True)#Search book 2005 by year fail
        logger.append("Search book 2005 by year fail")

        new_b = BookFactory.creat_book("test8", "myself", "No", "other", 1, 1, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit)  ###book added successfully
        logger.append("book added successfully")

        filter_list=title_stra.search("test8",books_list,True)#Search book test8 by name completed successfully
        logger.append("Search book test8 by name completed successfully")
        filter_list=author_stra.search("myself",books_list,True)#Search book myself by author completed successfully
        logger.append("Search book myself by author completed successfully")
        filter_list=genre_stra.search("other",books_list,True)#Search book other by genre completed successfully
        logger.append("Search book other by genre completed successfully")
        filter_list=year_stra.search("2005",books_list,True)#Search book 2005 by year completed successfully
        logger.append("Search book 2005 by year completed successfully")

        lend_book("test8")#book borrowed successfully
        logger.append("book borrowed successfully")

        return_book("test8")#book returns successfully
        logger.append("book returned successfully")

        return_book("test8")#book returns fail
        logger.append("book returned fail")

        remove_book("test8")#book removed successfully
        logger.append("book removed successfully")

        remove_book("test8")#book removed fail
        logger.append("book removed fail")



        with open('log.txt', 'r') as file:
            for line in file:
                log_txt.append(line.strip())

        self.assertTrue(len(log_txt)==len(logger))
        for i in range(len(log_txt)):
            print(log_txt[i])
            self.assertTrue(log_txt[i]==logger[i])


    '''
    This test checks if the library correctly manages the first available book in case of a book return 
    and verifies that the correct number of copies is adjusted when a book is returned and added back. 
    It also verifies if the book's availability status is updated accordingly.
    '''


    def test_return_first_or_add_first_ava_book(self):
        Librarian.init_library()
        new_b = BookFactory.creat_book("test9", "myself", "No", "other", 2, 2, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit)



        for i in books_list:
            if i.get_title()==new_b.get_title():
                lend_book("test9")
                lend_book("test9")
                print(i.get_is_loaned())

                self.assertTrue(i in loaned_list)
                self.assertTrue(i.get_available_copies()==0)

                return_book("test9")
                self.assertTrue(i not in loaned_list)
                self.assertTrue(i.get_available_copies()==1)

                lend_book("test9")
                self.assertTrue(i in loaned_list)
                self.assertTrue(i.get_available_copies()==0)

                add_book(new_b_dit)
                self.assertTrue(i not in loaned_list)
                self.assertTrue(i.get_available_copies()==2)
                self.assertTrue(i.get_copies() == 4)

        return_book("test9")
        return_book("test9")
        remove_book("test9")


    '''
    This test checks if the system properly handles and displays the results for books that are removed 
    or not found. It also verifies if the appropriate error message is shown when trying to return or 
    remove a book that is not in the system.
    '''

    def test_return_not_exist_book(self):
        Librarian.init_library()
        new_b = BookFactory.creat_book("test10", "myself", "No", "other", 2, 2, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit)
        for i in books_list:
            if i.get_title()==new_b.get_title():
                self.assertTrue(i in books_list)
                remove_book("test10")
                self.assertEqual(return_book("test10"),"book not found")








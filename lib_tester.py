import unittest

import Librarian
import Serarch_strategy

from Librarian import *
from Book import BookFactory

class MyTestCase(unittest.TestCase):



    def test_duplicated_user_name(self):
        c1 =["Dan", 26, "the_same", "1234"]
        Librarian.create_librarian(c1)
        c2 = ["ben", 30, "the_same", "1111"]
        self.assertTrue(check_user_name(c2[2]))

    def test_invalid_age(self):###########################################33
        with self.assertRaises(ValueError):
            c2 = ["ben", "aa", "the_same", "1111"]
            validate_input(c2[1],"age")
        with self.assertRaises(ValueError):
            c1 = ["Dan", -1, "dan12", "1234"]
            validate_input(c1[1],"age")

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

    def test_loaned_not_exist_book(self):
        b = lend_book("not exist book")
        self.assertTrue(b=="not found")

    #def test_return_not_exist_book(self):

    def test_loaned_unavailable_book(self):
        new_b = ["test1", "myself", "other", 2, 2005]
        Librarian.init_library()
        add_book(new_b)
        b=lend_book("test")
        self.assertTrue(b == "done")
        b=lend_book("test")
        self.assertTrue(b == "done")
        b=lend_book("test")
        self.assertTrue(b == "waiting list")


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


        # lend_book("test3")
        # lend_book("test3")
        for i in books_list:
            if i.get_title() == new_b.get_title():
                self.assertEqual(i.get_copies(),2)
                self.assertEqual(i.get_available_copies(), 0)

        #remove_book("test3") #################################need to add return and remove

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

    #def test_view_results(self):#########################dont know how to test
        #Librarian.init_library()


    def test_popularity_result(self):
        Librarian.init_library()
        popular=popular_books()
        print(popular[0].get_title())
        self.assertTrue(popular[0].get_title() == "1984")
        new_b = BookFactory.creat_book("test5", "myself", "No", "other", 10, 10, [], 2005)
        new_b_dit = [new_b.get_title(), new_b.get_author(), new_b.get_genre(), new_b.get_copies(), new_b.get_year()]
        add_book(new_b_dit)

        lend_book("test5")
        lend_book("test5")
        lend_book("test5")
        lend_book("test5")
        lend_book("test5")
        popular = popular_books()

        self.assertTrue(popular[0].get_title() == "1984")
        lend_book("test5")
        popular = popular_books()

        self.assertTrue(popular[0].get_title() == "test5")

        #############################################################need to add return and remove


    #def test_save_data_after_restart(self):##not sure this is possible


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

        ######################need to add return and remove


    #def test_return_ar_add_first_ava_book(self): ################cant yet

    def test_exceptions_raises(self):

        self.assertRaises(ValueError, validate_non_empty_data,"")

        self.assertRaises(ValueError,validate_input,"","non")
        self.assertRaises(ValueError, validate_input, "a", "non")
        self.assertRaises(ValueError, validate_input, -5, "age")
        self.assertRaises(ValueError, validate_input, -5, "copies")
        self.assertRaises(ValueError, validate_input, 11111, "phone")



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

        with open('log.txt', 'r') as file:
            for line in file:
                log_txt.append(line.strip())

        self.assertTrue(len(log_txt)==len(logger))
        for i in range(len(log_txt)):
            print(log_txt[i])
            self.assertTrue(log_txt[i]==logger[i])



        ##################need to return and remove









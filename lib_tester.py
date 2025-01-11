import unittest

import Librarian
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

        #remove_book("test3")

    #def test_search_new_book(self):

    #def test_search_results(self):

    #def test_unregistered_user(self):

    #def test_view_results(self):

    #def test_popularity_result(self):

    #def test_save_data_after_restart(self):##not sure this is possible

    #def test_loaned_last_ava_book(self):

    #def test_return_ar_add_first_ava_book(self):

    #def test_add_exist_book_with_loaned_copies(self):

    #def test_log(self):

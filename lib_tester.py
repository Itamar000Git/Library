import unittest

import Librarian
from Librarian import *


class MyTestCase(unittest.TestCase):


    def test_duplicated_user_name(self):
        c1 =["Dan", 26, "the_same", "1234"]
        Librarian.create_librarian(c1)
        c2 = ["ben", 30, "the_same", "1111"]
        self.assertTrue(check_user_name(c2[2]))

    def test_invalid_age(self):
        with self.assertRaises(TypeError):
            c2 = ["ben", "aa", "the_same", "1111"]
            validate_input(c2[1])
        with self.assertRaises(ValueError):
            c1 = ["Dan", -1, "dan12", "1234"]
            validate_input(c1[1])

    def test_cradential(self):
        c1 =["Dan", 26, "Dan12", "1234"]
        c2 = ["ben", 10, "ben21", "1111"]
        c1[3] = hashlib.sha256(c1[3].encode()).hexdigest()
        c2[3] = hashlib.sha256(c2[3].encode()).hexdigest()

        l1=Librarian.create_librarian(c1)
        l2=Librarian.create_librarian(c2)
        print(l1)
        self.assertTrue( check_password(l1.get_password(),"Dan12"))

        self.assertFalse(check_password(l2.get_password(),"Dan12"))
        self.assertTrue(check_password(l2.get_password(), "ben21"))

    def test_removed_loaned_book(self):#################3

        Librarian.init_library()
        result=remove_book("1984")
        self.assertTrue(result=="loaned")

        new_b=["test","myself","Fantasy",2,2005]
        add_book(new_b)
        result=remove_book("test")
        self.assertTrue(result=="found")

        result=remove_book("not exist book")
        self.assertTrue(result=="not found")

    #def test_add(self):





if __name__ == '__main__':
    unittest.main()

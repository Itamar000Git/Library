import unittest

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

    #def test_removed_loaned_book(self):#################3

    # def test_add(self):
    #     self.assertEqual(self.calc.add(1, 2), 3)
    #     self.assertEqual(self.calc.add(-1, 1), 0)
    #     self.assertEqual(self.calc.add(-1, -1), -2)
    #
    # def test_subtract(self):
    #     self.assertEqual(self.calc.subtract(10, 5), 5)
    #     self.assertEqual(self.calc.subtract(-1, 1), -2)
    #     self.assertEqual(self.calc.subtract(-1, -1), 0)
    #
    # def test_multiply(self):
    #     self.assertEqual(self.calc.multiply(3, 3), 9)
    #     self.assertEqual(self.calc.multiply(-1, 1), -1)
    #     self.assertEqual(self.calc.multiply(-1, -1), 1)
    #
    # def test_divide(self):
    #     self.assertEqual(self.calc.divide(10, 2), 5)
    #     self.assertEqual(self.calc.divide(-10, 2), -5)
    #     self.assertEqual(self.calc.divide(0, 1), 0)
    #
    #     with self.assertRaises(ValueError):  # Check for division by zero
    #         self.calc.divide(10, 0)




if __name__ == '__main__':
    unittest.main()

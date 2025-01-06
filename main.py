import Book
import Person
import csv
import pandas as pd
from Person import Customer
from Person import Person
from Person import Librarian
from Book import BookFactory
from Person import Librarian

import pandas as pd







def main():

    Librarian.init_library()

    # b1= Book.BookFactory.creat_book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 4, 1937)
    # b1 = Book.BookFactory.creat_book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 4, 1937)
    # print(b1)
    # print(b1.get_dic_copies())


    # df.loc[df["title"]=="The Catcher in the Rye","is_loaned"]="Yes"
    # df.to_csv("Books.csv",index=False)
    #print(df)

    #creates object that got from the csv




    # for i in books_list:
    #     if i.get_title()=="The Hobbit": ##chackes if copies changes
    #         print(i.get_title() +' '+str(i.get_copies()) + ' ' +str(i.get_dic_copies()))
    #
    #         i.add_copies(1)
    #         print(i.get_title() + ' ' + str(i.get_copies())+ ' ' +str(i.get_dic_copies()))


    #books_dict['The Hobbit']

    #title: str, author: str, genre: str, copies: int, year: int
    # with open('log.txt', 'a') as file:
    #     file.write("Appending a new line to the file.\n")


if __name__ == '__main__':
    main()
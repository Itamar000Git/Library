import tkinter as tk
from tkinter import messagebox

import Gui_lib
import Librarian
from Librarian import *
from add_books_gui import add_book_to_lib
from popular_books_gui import popular_books_from_lib
from remove_book import remove_book_from_lib
from search_book_gui import search_book_in_lib
from view_books_gui import view_books_from_lib


def menu_window():
    menu_win = tk.Tk()
    menu_win.title("menu")
    menu_win.geometry("300x500")
    menu_win.config(bg="#f0f0f0")


    def add_book_submit():
        menu_win.withdraw()
        add_book_to_lib()
        #menu_win.deiconify()
    def remove_book_submit():
        menu_win.withdraw()
        remove_book_from_lib()
    def search_book_submit():
        menu_win.withdraw()
        search_book_in_lib()
    def view_book_submit():
        menu_win.withdraw()
        view_books_from_lib()
    def popular_book_submit():
        menu_win.withdraw()
        popular_books_from_lib()
    def logout_submit():
        menu_win.withdraw()
        messagebox.showinfo("Logout", "Logged out")
        Gui_lib.root.deiconify()


    Add_button = tk.Button(menu_win, text="Add Book", font=("David", 20),width=20,command = add_book_submit, bg="#4CAF50", fg="white")
    Add_button.pack(pady=5)

    Remove_button = tk.Button(menu_win, text="Remove Book", font=("David", 20),width=20,command=remove_book_submit, bg="#4CAF50", fg="white")
    Remove_button.pack(pady=5)

    Search_button = tk.Button(menu_win, text="Search Book", font=("David", 20),width=20,command=search_book_submit, bg="#4CAF50", fg="white")
    Search_button.pack(pady=5)

    View_button = tk.Button(menu_win, text="View Books", font=("David", 20),width=20,command=view_book_submit, bg="#4CAF50", fg="white")
    View_button.pack(pady=5)

    Lend_button = tk.Button(menu_win, text="Lend Book", font=("David", 20),width=20,command=lend_book(), bg="#4CAF50", fg="white")
    Lend_button.pack(pady=5)

    Return_button = tk.Button(menu_win, text="Return Book", font=("David", 20),width=20,command=return_book(), bg="#4CAF50", fg="white")
    Return_button.pack(pady=5)

    Logout_button = tk.Button(menu_win, text="Logout", font=("David", 20),width=20,command=logout_submit, bg="#4CAF50", fg="white")
    Logout_button.pack(pady=5)

    popular_button = tk.Button(menu_win, text="popular books", font=("David", 20),width=20,command=popular_book_submit, bg="#4CAF50", fg="white")
    popular_button.pack(pady=5)




    def back_to_main():
        menu_win.destroy()
        Gui_lib.root.deiconify()  ##############################################

    back_button = tk.Button(menu_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

   
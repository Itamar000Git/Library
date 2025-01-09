import tkinter as tk
from tkinter import messagebox

import Gui_menu
import Librarian
import popular_books_gui
from popular_books_gui import *
from Librarian import *

def view_all_books():
    view_all_books_win = tk.Tk()
    view_all_books_win.title("Books list")
    view_all_books_win.geometry("600x620")
    view_all_books_win.config(bg="#f0f0f0")
    entry_label = tk.Label(view_all_books_win, text="All Books list", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)

    text_widget = tk.Text(view_all_books_win, font=("David", 12), height=32, width=70)
    text_widget.pack(pady=1)

    text_widget.delete(1.0, tk.END)
    i = 1
    for item in Librarian.books_list:
        text_widget.insert(tk.END, f"{i}. {item}\n")
        i += 1

    def back_to_main():
        view_all_books_win.destroy()
        view_books_from_lib()

    back_button = tk.Button(view_all_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500",
                            fg="white")
    back_button.pack(pady=1)

def view_available_books():

    view_ava_books_win = tk.Tk()
    view_ava_books_win.title("Available Books list")
    view_ava_books_win.geometry("600x400")
    view_ava_books_win.config(bg="#f0f0f0")
    entry_label = tk.Label(view_ava_books_win, text="All available books", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)

    text_widget = tk.Text(view_ava_books_win, font=("David", 12), height=20, width=70)
    text_widget.pack(pady=1)

    text_widget.delete(1.0, tk.END)
    i = 1
    for item in Librarian.available_list:
        text_widget.insert(tk.END, f"{i}. {item}\n")
        i += 1

    def back_to_main():
        view_ava_books_win.destroy()
        view_books_from_lib()

    back_button = tk.Button(view_ava_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500",fg="white")
    back_button.pack(pady=1)




def view_loaned_books():

    view_loaned_books_win = tk.Tk()
    view_loaned_books_win.title("Loaned Books list")
    view_loaned_books_win.geometry("600x400")
    view_loaned_books_win.config(bg="#f0f0f0")
    entry_label = tk.Label(view_loaned_books_win, text="All loaned books", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)

    text_widget = tk.Text(view_loaned_books_win, font=("David", 12), height=20, width=70)
    text_widget.pack(pady=1)

    text_widget.delete(1.0, tk.END)
    i = 1
    for item in Librarian.loaned_list:
        text_widget.insert(tk.END, f"{i}. {item}\n")
        i += 1

    def back_to_main():
        view_loaned_books_win.destroy()
        view_books_from_lib()

    back_button = tk.Button(view_loaned_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500",fg="white")
    back_button.pack(pady=1)














def view_books_from_lib():

    view_books_win = tk.Tk()
    view_books_win.title("view books")
    view_books_win.geometry("300x300")
    view_books_win.config(bg="#f0f0f0")


    def all_book_submit():
        view_books_win.withdraw()
        view_all_books()
    def loaned_book_submit():
        view_books_win.withdraw()
        view_loaned_books()
    def available_book_submit():
        view_books_win.withdraw()
        view_available_books()

    def popular_book_submit():
        view_books_win.withdraw()
        popular_books_gui.popular_books_from_lib()



    All_button = tk.Button(view_books_win, text="All Books", font=("David", 20),width=20,command = all_book_submit, bg="#4CAF50", fg="white")
    All_button.pack(pady=5)

    Loaned_button = tk.Button(view_books_win, text="Loaned Books", font=("David", 20),width=20,command=loaned_book_submit, bg="#4CAF50", fg="white")
    Loaned_button.pack(pady=5)

    Available_button = tk.Button(view_books_win, text="Available Books", font=("David", 20),width=20,command=available_book_submit, bg="#4CAF50", fg="white")
    Available_button.pack(pady=5)

    Popular_button = tk.Button(view_books_win, text="Popular Books", font=("David", 20),width=20,command=popular_book_submit, bg="#4CAF50", fg="white")
    Popular_button.pack(pady=5)


    def back_to_main():
        view_books_win.destroy()
        Gui_menu.menu_window()

    back_button = tk.Button(view_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

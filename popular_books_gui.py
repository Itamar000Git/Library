import tkinter as tk
from tkinter import messagebox

import Gui_menu
import Librarian
import view_books_gui
from Librarian import *
#from Librarian import remove_book, validate_non_empty_data
from view_books_gui import view_books_from_lib


def popular_books_from_lib():
    popular_books_win = tk.Tk()
    popular_books_win.title("Top 10 popular books")
    popular_books_win.geometry("600x400")
    popular_books_win.config(bg="#f0f0f0")
    entry_label = tk.Label(popular_books_win, text="Top 10 popular books", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)

    text_widget = tk.Text(popular_books_win, font=("David", 12), height=20, width=70)###############
    text_widget.pack(pady=1)
    top_ten=[]
    top_ten= popular_books()



    text_widget.delete(1.0, tk.END)
    i=1
    for item in top_ten:
        text_widget.insert(tk.END, f"{i}. {item}\n")
        i+=1
        if i == 11:
            break



    def back_to_main():
        popular_books_win.destroy()
        view_books_gui.view_books_from_lib()

    back_button = tk.Button(popular_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

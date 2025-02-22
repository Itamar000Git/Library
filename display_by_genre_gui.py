import tkinter as tk
from tkinter import messagebox

import Serarch_strategy
from Librarian import *
from view_books_gui import view_books_by_genre_from_lib

'''
This is the window that display all the books sorted by chosen genre.
The "genre_books" except the genre and use the search strategy to get full list from the asked genre.'''
def genre_books(genre):
    try:
        #genre_books_win = tk.Tk()
        genre_books_win=tk.Toplevel()
        genre_books_win.title(f"{genre} Books list")
        genre_books_win.geometry("600x400")
        genre_books_win.config(bg="#f0f0f0")
        entry_label = tk.Label(genre_books_win, text=f"{genre} books", font=("David", 12), bg="#f0f0f0")
        entry_label.pack(pady=1)

        text_widget = tk.Text(genre_books_win, font=("David", 12), height=20, width=80)
        text_widget.pack(pady=1)

        text_widget.delete(1.0, tk.END)
        stra=Serarch_strategy.search_book_genre()
        genre_list=stra.search(genre,books_list,False)

        i = 1
        for item in genre_list:
            text_widget.insert(tk.END, f"{i}. {item}\n")
            i += 1

        def back_to_main():
            genre_books_win.destroy()
            view_books_by_genre_from_lib()

        back_button = tk.Button(genre_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500",fg="white")
        back_button.pack(pady=1)

        with open('log.txt', 'a') as logger:
            logger.write("Displayed book by category successfully\n")

    except:
            with open('log.txt', 'a') as logger:
                logger.write("Displayed book by category fail\n")
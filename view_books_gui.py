import tkinter as tk
from tkinter import messagebox
from Librarian import *
import Gui_menu
import Librarian
import popular_books_gui

from popular_books_gui import *


def view_all_books():
   # view_all_books_win = tk.Tk()
   try:
        view_all_books_win=tk.Toplevel()
        view_all_books_win.title("Books list")
        view_all_books_win.geometry("600x620")
        view_all_books_win.config(bg="#f0f0f0")
        entry_label = tk.Label(view_all_books_win, text="All Books list", font=("David", 12), bg="#f0f0f0")
        entry_label.pack(pady=1)

        text_widget = tk.Text(view_all_books_win, font=("David", 12), height=32, width=80)
        text_widget.pack(pady=1)

        text_widget.delete(1.0, tk.END)
        i = 1
        for item in books_list:
            text_widget.insert(tk.END, f"{i}. {item}\n")
            i += 1

        def back_to_main():
            view_all_books_win.destroy()
            view_books_from_lib()

        back_button = tk.Button(view_all_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500",
                                fg="white")
        back_button.pack(pady=1)
        with open('log.txt', 'a') as logger:
            logger.write("Displayed all books successfully\n")
   except:
       with open('log.txt', 'a') as logger:
           logger.write("Displayed all books fail\n")

def view_available_books():

    #view_ava_books_win = tk.Tk()
    try:
        view_ava_books_win=tk.Toplevel()
        view_ava_books_win.title("Available Books list")
        view_ava_books_win.geometry("600x400")
        view_ava_books_win.config(bg="#f0f0f0")
        entry_label = tk.Label(view_ava_books_win, text="All available books", font=("David", 12), bg="#f0f0f0")
        entry_label.pack(pady=1)

        text_widget = tk.Text(view_ava_books_win, font=("David", 12), height=20, width=80)
        text_widget.pack(pady=1)

        text_widget.delete(1.0, tk.END)
        i = 1
        for item in available_list:
            text_widget.insert(tk.END, f"{i}. {item}\n")
            i += 1

        def back_to_main():
            view_ava_books_win.destroy()
            view_books_from_lib()

        back_button = tk.Button(view_ava_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500",fg="white")
        back_button.pack(pady=1)

        with open('log.txt', 'a') as logger:
            logger.write("Displayed available books successfully\n")
    except:
        with open('log.txt', 'a') as logger:
            logger.write("Displayed available books fail\n")




def view_loaned_books():

    try:
        view_loaned_books_win=tk.Toplevel()
        view_loaned_books_win.title("Loaned Books list")
        view_loaned_books_win.geometry("600x400")
        view_loaned_books_win.config(bg="#f0f0f0")
        entry_label = tk.Label(view_loaned_books_win, text="All loaned books", font=("David", 12), bg="#f0f0f0")
        entry_label.pack(pady=1)

        text_widget = tk.Text(view_loaned_books_win, font=("David", 12), height=20, width=80)
        text_widget.pack(pady=1)

        text_widget.delete(1.0, tk.END)
        i = 1
        for item in loaned_list:
            text_widget.insert(tk.END, f"{i}. {item}\n")
            i += 1

        def back_to_main():
            view_loaned_books_win.destroy()
            view_books_from_lib()

        back_button = tk.Button(view_loaned_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500",fg="white")
        back_button.pack(pady=1)

        with open('log.txt', 'a') as logger:
            logger.write("Displayed borrowed books successfully\n")
    except:
        with open('log.txt', 'a') as logger:
            logger.write("Displayed borrowed books fail\n")


def view_books_by_genre_from_lib():
    from display_by_genre_gui import genre_books
    #genre_books_win = tk.Tk()
    genre_books_win=tk.Toplevel()
    genre_books_win.title("books by genre")
    genre_books_win.geometry("700x350")
    genre_books_win.config(bg="#f0f0f0")


    def fiction_submit():
        genre_books_win.withdraw()
        genre_books("Fiction")
    def dystopian_submit():
        genre_books_win.withdraw()
        genre_books("Dystopian")
    def classic_submit():
        genre_books_win.withdraw()
        genre_books("Classic")
    def adventure_submit():
        genre_books_win.withdraw()
        genre_books("Adventure")
    def historical_fiction_submit():
        genre_books_win.withdraw()
        genre_books("Historical Fiction")
    def psychological_drama_submit():
        genre_books_win.withdraw()
        genre_books("Psychological Drama")
    def philosophy_submit():
        genre_books_win.withdraw()
        genre_books("Philosophy")
    def epic_poetry_submit():
        genre_books_win.withdraw()
        genre_books("Epic Poetry")
    def gothic_fiction_submit():
        genre_books_win.withdraw()
        genre_books("Gothic Fiction")
    def gothic_romance_submit():
        genre_books_win.withdraw()
        genre_books("Gothic Romance")
    def romance_submit():
        genre_books_win.withdraw()
        genre_books("Romance")
    def realism_submit():
        genre_books_win.withdraw()
        genre_books("Realism")
    def modernism_submit():
        genre_books_win.withdraw()
        genre_books("Modernism")
    def satire_submit():
        genre_books_win.withdraw()
        genre_books("Satire")
    def science_fiction_submit():
        genre_books_win.withdraw()
        genre_books("Science Fiction")
    def tragedy_submit():
        genre_books_win.withdraw()
        genre_books("Tragedy")
    def fantasy_submit():
        genre_books_win.withdraw()
        genre_books("Fantasy")
    def other_submit():
        genre_books_win.withdraw()
        genre_books("other")


    fiction_button = tk.Button(genre_books_win, text="Fiction", font=("David", 12), height=2, width=20,command=fiction_submit,bg="#37a8c8", fg="white")
    fiction_button.grid(row=1, column=0, padx=3, pady=3)

    dystopian_button = tk.Button(genre_books_win, text="Dystopian", font=("David", 12), height=2, width=20,command=dystopian_submit,bg="#37a8c8", fg="white")
    dystopian_button.grid(row=1, column=1, padx=3, pady=3)

    classic_button = tk.Button(genre_books_win, text="Classic", font=("David", 12), height=2, width=20,command=classic_submit,bg="#37a8c8", fg="white")
    classic_button.grid(row=1, column=2, padx=3, pady=3)

    adventure_button = tk.Button(genre_books_win, text="Adventure", font=("David", 12), height=2, width=20,command=adventure_submit,bg="#37a8c8", fg="white")
    adventure_button.grid(row=1, column=3, padx=3, pady=3)



    historical_fiction_button = tk.Button(genre_books_win, text="Historical Fiction", font=("David", 12), height=2, width=20,command=historical_fiction_submit,bg="#37a8c8", fg="white")
    historical_fiction_button.grid(row=2, column=0, padx=3, pady=3)

    psychological_drama_button = tk.Button(genre_books_win, text="Psychological Drama", font=("David", 12), height=2, width=20,command=psychological_drama_submit,bg="#37a8c8", fg="white")
    psychological_drama_button.grid(row=2, column=1, padx=3, pady=3)

    philosophy_button = tk.Button(genre_books_win, text="Philosophy", font=("David", 12), height=2, width=20,command=philosophy_submit,bg="#37a8c8", fg="white")
    philosophy_button.grid(row=2, column=2, padx=3, pady=3)

    epic_poetry_button = tk.Button(genre_books_win, text="Epic Poetry", font=("David", 12), height=2, width=20,command=epic_poetry_submit,bg="#37a8c8", fg="white")
    epic_poetry_button.grid(row=2, column=3, padx=3, pady=3)


    gothic_romance_button = tk.Button(genre_books_win, text="Gothic Romance", font=("David", 12), height=2, width=20,command=gothic_romance_submit,bg="#37a8c8", fg="white")
    gothic_romance_button.grid(row=3, column=0, padx=3, pady=3)

    realism_button = tk.Button(genre_books_win, text="Realism", font=("David", 12), height=2, width=20,command=realism_submit,bg="#37a8c8", fg="white")
    realism_button.grid(row=3, column=1, padx=3, pady=3)

    modernism_button = tk.Button(genre_books_win, text="Modernism", font=("David", 12), height=2, width=20,command=modernism_submit,bg="#37a8c8", fg="white")
    modernism_button.grid(row=3, column=2, padx=3, pady=3)

    satire_button = tk.Button(genre_books_win, text="Satire", font=("David", 12), height=2, width=20,command=satire_submit,bg="#37a8c8", fg="white")
    satire_button.grid(row=3, column=3, padx=3, pady=3)



    tragedy_button = tk.Button(genre_books_win, text="Tragedy", font=("David", 12), height=2, width=20,command=tragedy_submit,bg="#37a8c8", fg="white")
    tragedy_button.grid(row=4, column=0, padx=3, pady=3)

    fantasy_button = tk.Button(genre_books_win, text="Fantasy", font=("David", 12), height=2, width=20,command=fantasy_submit,bg="#37a8c8", fg="white")
    fantasy_button.grid(row=4, column=1, padx=3, pady=3)

    romance_button = tk.Button(genre_books_win, text="Romance", font=("David", 12), height=2, width=20,command=romance_submit,bg="#37a8c8", fg="white")
    romance_button.grid(row=4, column=2, padx=3, pady=3)

    science_fiction_button = tk.Button(genre_books_win, text="Science Fiction", font=("David", 12), height=2, width=20,command=science_fiction_submit,bg="#37a8c8", fg="white")
    science_fiction_button.grid(row=4, column=3, padx=3, pady=3)


    gothic_fiction_button = tk.Button(genre_books_win, text="Gothic Fiction", font=("David", 12), height=2, width=20,command=gothic_fiction_submit,bg="#37a8c8", fg="white")
    gothic_fiction_button.grid(row=5, column=0, padx=3, pady=3)

    other_button = tk.Button(genre_books_win, text="Other", font=("David", 12), height=2, width=20,command=other_submit,bg="#37a8c8", fg="white")
    other_button.grid(row=5, column=1, padx=3, pady=3)

    for i in range(0, 6):  # Iterate over all rows and columns in the grid
        if i != 0:
            genre_books_win.grid_rowconfigure(i, weight=1)  # Assign a weight to each row to make them resizable
        genre_books_win.grid_columnconfigure(i, weight=1)  # Assign a weight to each column to make them resizable

    def back_to_main():
        genre_books_win.destroy()
        view_books_from_lib()

    back_button = tk.Button(genre_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.grid(row=5, column=2, padx=3, pady=3)











def view_books_from_lib():

    #view_books_win = tk.Tk()
    view_books_win=tk.Toplevel()
    view_books_win.title("view books")
    view_books_win.geometry("300x330")
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

    def book_by_genre_submit():
        view_books_win.withdraw()
        view_books_by_genre_from_lib()



    All_button = tk.Button(view_books_win, text="All Books", font=("David", 20),width=20,command = all_book_submit, bg="#4CAF50", fg="white")
    All_button.pack(pady=5)

    Loaned_button = tk.Button(view_books_win, text="Loaned Books", font=("David", 20),width=20,command=loaned_book_submit, bg="#4CAF50", fg="white")
    Loaned_button.pack(pady=5)

    Available_button = tk.Button(view_books_win, text="Available Books", font=("David", 20),width=20,command=available_book_submit, bg="#4CAF50", fg="white")
    Available_button.pack(pady=5)

    Popular_button = tk.Button(view_books_win, text="Popular Books", font=("David", 20),width=20,command=popular_book_submit, bg="#4CAF50", fg="white")
    Popular_button.pack(pady=5)

    genre_button = tk.Button(view_books_win, text="Books by genre", font=("David", 20),width=20,command=book_by_genre_submit, bg="#4CAF50", fg="white")
    genre_button.pack(pady=5)


    def back_to_main():
        view_books_win.destroy()
        Gui_menu.menu_window()

    back_button = tk.Button(view_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

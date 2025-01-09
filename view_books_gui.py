import tkinter as tk
from tkinter import messagebox

import Gui_menu
import Librarian
from Librarian import remove_book, validate_non_empty_data


def view_books_from_lib():
    view_books_win = tk.Tk()
    view_books_win.title("Books list")
    view_books_win.geometry("600x620")
    view_books_win.config(bg="#f0f0f0")
    entry_label = tk.Label(view_books_win, text="Books list", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)

    text_widget = tk.Text(view_books_win, font=("David", 12), height=32, width=70)
    text_widget.pack(pady=1)


    text_widget.delete(1.0, tk.END)
    i=1
    for item in Librarian.books_list:
        text_widget.insert(tk.END, f"{i}. {item}\n")
        i+=1
    def back_to_main():
        view_books_win.destroy()
        Gui_menu.menu_window()  ##############################################

    back_button = tk.Button(view_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

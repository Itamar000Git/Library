import tkinter as tk
from tkinter import messagebox

import Gui_menu
from Librarian import add_book


def add_book_to_lib():
    add_win = tk.Tk()
    add_win.title("new book")
    add_win.geometry("300x300")
    add_win.config(bg="#f0f0f0")
    entry_label = tk.Label(add_win, text="Title", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    title_entry = tk.Entry(add_win, font=("David", 12), width=20)
    title_entry.pack(pady=1)

    entry_label = tk.Label(add_win, text="Author", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    author_entry = tk.Entry(add_win, font=("David", 12), width=20)
    author_entry.pack(pady=1)

    entry_label = tk.Label(add_win, text="Genre", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    genre_entry = tk.Entry(add_win, font=("David", 12), width=20)
    genre_entry.pack(pady=1)

    entry_label = tk.Label(add_win, text="Copies", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    copies_entry = tk.Entry(add_win, font=("David", 12), width=20)
    copies_entry.pack(pady=1)

    entry_label = tk.Label(add_win, text="Year", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    year_entry = tk.Entry(add_win, font=("David", 12), width=20)
    year_entry.pack(pady=1)
    new_book = []
    def submit():
        title_input = title_entry.get()
        new_book.append(str(title_input))
        print(f"Entered book title: {title_input}")

        author_input = author_entry.get()
        new_book.append(str(author_input))
        print(f"Entered book author: {author_input}")

        genre_input = genre_entry.get()
        new_book.append(str(genre_input))
        print(f"Entered book genre: {genre_input}")

        copies_input = copies_entry.get()
        new_book.append(int(copies_input)) #####################need to make sur its int
        print(f"Entered book copies: {copies_input}")

        year_input = year_entry.get()
        new_book.append(int(year_input))##################### need to check validate
        print(f"Entered book year: {year_input}")
        b=add_book(new_book)
        new_book.clear()
        if b == "new":
            messagebox.showinfo("Success", "Book added successfully")
        elif b == "exist":
            messagebox.showinfo("Success", "Book book already exists, another copy added")
        else:
            messagebox.showerror("Error", "Book not added")
        add_win.destroy()
        Gui_menu.menu_window()



    submit_button = tk.Button(add_win, text="Submit", font=("David", 12),command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        add_win.destroy()
        Gui_menu.menu_window() ##############################################

    back_button = tk.Button(add_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)
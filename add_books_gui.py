import tkinter as tk
from tkinter import messagebox

import Gui_menu
from Librarian import add_book, validate_non_empty_data, validate_input

'''
Gui window that implement adding book function.
The function opens 5 entry's and keep the value when we click the submit button.
The window support "back" function.'''
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
    # When we click on submit al the values from the entries insert to the variables.
    #the function take care exceptions like invalid input.
    def submit():
        try:
            title_input = title_entry.get()
            validate_non_empty_data(title_input)
            new_book.append(str(title_input))
            print(f"Entered book title: {title_input}")

            author_input = author_entry.get()
            validate_non_empty_data(author_input)
            new_book.append(str(author_input))
            print(f"Entered book author: {author_input}")

            genre_input = genre_entry.get()
            validate_non_empty_data(genre_input)
            new_book.append(str(genre_input))
            print(f"Entered book genre: {genre_input}")

            copies_input = copies_entry.get()
            validate_input(int(copies_input),"copies")
            new_book.append(int(copies_input)) #####################need to make sur its int
            print(f"Entered book copies: {copies_input}")

            year_input = year_entry.get()
            validate_input(int(year_input),"year")
            new_book.append(int(year_input))##################### need to check validate
            print(f"Entered book year: {year_input}")


            b=add_book(new_book) #send as input a list that include all the book fields. "b" is string that help us indicate what add book done.
            new_book.clear()
            if b == "new":
                messagebox.showinfo("Success", "Book added successfully")
            elif b == "exist":
                messagebox.showinfo("Success", "Book book already exists, another copy added")
            else:
                messagebox.showerror("Error", "Book not added")
        except ValueError as e:
            print(e)
            messagebox.showerror("Error", e)
            add_win.destroy() #if there is any problem close the specific window and go back to the start
            add_book_to_lib()
        add_win.destroy() # if we finished the process of adding book
        Gui_menu.menu_window()



    submit_button = tk.Button(add_win, text="Submit", font=("David", 12),command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        add_win.destroy()
        Gui_menu.menu_window()

    back_button = tk.Button(add_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)
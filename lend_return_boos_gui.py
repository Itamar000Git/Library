import tkinter as tk
from tkinter import messagebox

import Gui_menu
from Librarian import remove_book, validate_non_empty_data, lend_book


def lend_books_from_lib():
    lend_win = tk.Tk()
    lend_win.title("lend book")
    lend_win.geometry("300x300")
    lend_win.config(bg="#f0f0f0")
    entry_label = tk.Label(lend_win, text="Title", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    title_entry = tk.Entry(lend_win, font=("David", 12), width=20)
    title_entry.pack(pady=1)


    def submit():

        title_input = title_entry.get()
        try:
            validate_non_empty_data(title_input)
        except ValueError as e:
            messagebox.showerror("Error", e)
            lend_win.destroy()
            lend_books_from_lib()
            return



        print(f"Entered book title: {title_input}")
        # b=remove_book(title_input)
        # if b=="found":
        #     messagebox.showinfo("Success", "Book successfully removed")
        # elif b=="not found":
        #     messagebox.showerror("Error", "Book not in the system")
        # elif b=="loaned":
        #     messagebox.showerror("Error", "Book loaned")
        lend_win.destroy()
        Gui_menu.menu_window()


    submit_button = tk.Button(lend_win, text="Submit", font=("David", 12), command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        lend_win.destroy()
        Gui_menu.menu_window()  ##############################################

    back_button = tk.Button(lend_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)



def return_books_from_lib():
    return_win = tk.Tk()
    return_win.title("return book")
    return_win.geometry("300x300")
    return_win.config(bg="#f0f0f0")
    entry_label = tk.Label(return_win, text="Title", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    title_entry = tk.Entry(return_win, font=("David", 12), width=20)
    title_entry.pack(pady=1)


    def submit():

        title_input = title_entry.get()
        try:
            validate_non_empty_data(title_input)
        except ValueError as e:
            messagebox.showerror("Error", e)
            return_win.destroy()
            return_books_from_lib()
            return



        print(f"Entered book title: {title_input}")
        # b=remove_book(title_input)
        # if b=="found":
        #     messagebox.showinfo("Success", "Book successfully removed")
        # elif b=="not found":
        #     messagebox.showerror("Error", "Book not in the system")
        # elif b=="loaned":
        #     messagebox.showerror("Error", "Book loaned")
        return_win.destroy()
        Gui_menu.menu_window()


    submit_button = tk.Button(return_win, text="Submit", font=("David", 12), command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        return_win.destroy()
        Gui_menu.menu_window()  ##############################################

    back_button = tk.Button(return_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

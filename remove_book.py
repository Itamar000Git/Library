import tkinter as tk
from tkinter import messagebox

import Gui_menu
from Librarian import *
'''
This function creates a window for removing a book from the library by its title. 
The user enters the title of the book they want to remove, and the input is validated. 
Based on whether the book is found, loaned, or not in the system, an appropriate message is shown, 
and the book is removed from the library if applicable. After the operation, the user is returned to the main menu.
'''

def remove_book_from_lib():
    #remove_win = tk.Tk()
    remove_win=tk.Toplevel()
    remove_win.title("remove book")
    remove_win.geometry("300x300")
    remove_win.config(bg="#f0f0f0")
    entry_label = tk.Label(remove_win, text="Title", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    title_entry = tk.Entry(remove_win, font=("David", 12), width=20)
    title_entry.pack(pady=1)


    def submit():


        try:
            title_input = title_entry.get()
            validate_non_empty_data(title_input)
        except ValueError as e:
            messagebox.showerror("Error", e)
            remove_win.destroy()
            remove_book_from_lib()
            return

        #new_book.append(str(title_input))

        print(f"Entered book title: {title_input}")
        b=remove_book(title_input)
        if b=="found":
            messagebox.showinfo("Success", "Book successfully removed")
        elif b=="not found":
            messagebox.showerror("Error", "Book not in the system")
        elif b=="loaned":
            messagebox.showerror("Error", "Book loaned")
        remove_win.destroy()
        Gui_menu.menu_window()


    submit_button = tk.Button(remove_win, text="Submit", font=("David", 12), command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        remove_win.destroy()
        Gui_menu.menu_window()

    back_button = tk.Button(remove_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

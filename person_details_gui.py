import tkinter as tk
from tkinter import messagebox

import Gui_menu
from Librarian import validate_non_empty_data, lend_book, validate_input, update_files_from_list, loaned_list, \
    available_list, books_list


def get_person_details(book):
    person_win = tk.Tk()
    person_win.title("person details")
    person_win.geometry("300x300")
    person_win.config(bg="#f0f0f0")

    entry_label = tk.Label(person_win, text="full name", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    full_name_entry = tk.Entry(person_win, font=("David", 12), width=20)
    full_name_entry.pack(pady=1)

    entry_label = tk.Label(person_win, text="phone number", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    phone_entry = tk.Entry(person_win, font=("David", 12), width=20)
    phone_entry.pack(pady=1)

    def submit1():
        person_dits=[]

        try:
            full_nume_input = full_name_entry.get()
            validate_non_empty_data(full_nume_input)
            person_dits.append(full_nume_input)
        except ValueError as e:
            messagebox.showerror("Error", e)
            person_win.destroy()
            get_person_details(book)
            return


        try:
            phone_input = phone_entry.get()
            validate_input(int(phone_input),"phone")
            person_dits.append(phone_input)
        except ValueError as e:
            messagebox.showerror("Error", e)
            person_win.destroy()
            get_person_details(book)
            return

        per_dict={str(person_dits[0]):str(person_dits[1])}

        #mystr=str(person_dits[0])+' : '+str(person_dits[1]+',')
        book.get_waiting_list().append(per_dict)
        #print(book.get_waiting_list())
        update_files_from_list(loaned_list, "loaned_books.csv")
        update_files_from_list(available_list, "available_books.csv")
        update_files_from_list(books_list, "books.csv")

        person_win.destroy()
        Gui_menu.menu_window()
        return person_dits


    submit_button = tk.Button(person_win, text="Submit", font=("David", 12), command=submit1, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        person_win.destroy()
        Gui_menu.menu_window()  ##############################################

    back_button = tk.Button(person_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

    messagebox.showinfo("unavailable", "please enter your details for waiting list")


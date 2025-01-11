import tkinter as tk
from tkinter import messagebox

import Gui_menu
from Librarian import validate_non_empty_data, lend_book, validate_input, loaned_list, available_list, books_list, \
    update_files_from_list


def get_person_details(title):

    person_win=tk.Toplevel()
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
        full_name_input = full_name_entry.get()
        try:
            validate_non_empty_data(full_name_input)
            person_dits.append(full_name_input)
        except ValueError as e:
            messagebox.showerror("Error", e)
            person_win.destroy()
            get_person_details(title)
            return


        try:
            phone_input = phone_entry.get()
            validate_input(int(phone_input),"phone")
            person_dits.append(phone_input)
        except ValueError as e:
            messagebox.showerror("Error", e)
            person_win.destroy()
            get_person_details(title)
            return

        per_dict={str(person_dits[0]):str(person_dits[1])}

        for i in books_list:
            if i.get_title()==title:
                if len(i.get_waiting_list())>0:
                    if i.get_waiting_list()[0] == 'nan':
                        i.get_waiting_list().remove(i)
                i.get_waiting_list().append(per_dict)

        messagebox.showinfo("info", "You are listed to the waiting list successfully.")

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
        Gui_menu.menu_window()

    back_button = tk.Button(person_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

    messagebox.showinfo("unavailable", "please enter your details for waiting list")


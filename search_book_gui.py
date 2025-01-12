import tkinter as tk
from tkinter import messagebox

import Gui_menu
import Librarian
from Librarian import remove_book, validate_non_empty_data, validate_input
from Serarch_strategy import search_book_title, search_book_author, search_book_genre, search_book_year

'''
This function allows users to search for books in the library based on four criteria: Title, Author, Genre, or Year. 
It creates a window with entry fields for each of the criteria and provides a Submit button for each. 
When the user submits a search query, the corresponding search function is called, and results are displayed in a new window. 
If no results are found, an informational message is shown. In case of an error, an error message is displayed, and the user can try again.
'''
def search_book_in_lib():
    #search_books_win = tk.Tk()
    search_books_win=tk.Toplevel()
    search_books_win.title("Search book")
    search_books_win.geometry("300x390")
    search_books_win.config(bg="#f0f0f0")

    def submit_title():
        title_stra = search_book_title()
        try:
            title_input = title_entry.get()
            validate_non_empty_data(title_input)
            print(str(title_input))

            result=title_stra.search(title_input, Librarian.books_list,True)
            for i in result:
                print(i.__str__())

            if len(result)>0:
                view_search(result)
            else:
                messagebox.showinfo(title="No result", message="No result")
                search_book_in_lib()

            search_books_win.withdraw()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            print(e)
            search_books_win.destroy()
            search_book_in_lib()




    def submit_author():
        author_stra = search_book_author()
        try:
            author_input = author_entry.get()
            validate_non_empty_data(author_input)
            print(str(author_input))

            result =  author_stra.search( author_input, Librarian.books_list,True)
            for i in result:
                print(i.__str__())

            if len(result)>0:
                view_search(result)
            else:
                messagebox.showinfo(title="No result", message="No result")
                search_book_in_lib()
            search_books_win.withdraw()


        except ValueError as e:
            messagebox.showerror("Error", str(e))
            print(e)
            search_books_win.destroy()
            search_book_in_lib()

    def submit_genre():
        genre_stra = search_book_genre()
        try:
            genre_input = genre_entry.get()
            validate_non_empty_data(genre_input)
            print(str(genre_input))

            result =  genre_stra.search( genre_input, Librarian.books_list,True)
            for i in result:
                print(i.__str__())

            if len(result) > 0:
                view_search(result)
            else:
                messagebox.showinfo(title="No result", message="No result")################################
                search_book_in_lib()

            search_books_win.withdraw()


        except ValueError as e:
            messagebox.showerror("Error", str(e))
            print(e)
            search_books_win.withdraw()
            search_book_in_lib()




    def submit_year():
        year_stra = search_book_year()
        try:
            year_input = year_entry.get()
            validate_input(int(year_input),"year")
            print(str(year_input))

            result =  year_stra.search( year_input, Librarian.books_list,True)
            for i in result:
                print(i.__str__())

            if len(result) > 0:
                view_search(result)
            else:
                messagebox.showinfo(title="No result", message="No result")
                search_book_in_lib()

            search_books_win.withdraw()
        except ValueError as e:
            messagebox.showerror("Error", str(e))
            print(e)
            search_books_win.destroy()
            search_book_in_lib()


    entry_label = tk.Label(search_books_win, text="Title", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    title_entry = tk.Entry(search_books_win, font=("David", 12), width=20)
    title_entry.pack(pady=1)
    submit_title_button = tk.Button(search_books_win, text="Submit", font=("David", 12),command=submit_title, bg="#4CAF50", fg="white")
    submit_title_button.pack(pady=1)

    entry_label = tk.Label(search_books_win, text="Author", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    author_entry = tk.Entry(search_books_win, font=("David", 12), width=20)
    author_entry.pack(pady=1)
    submit_author_button = tk.Button(search_books_win, text="Submit", font=("David", 12),command=submit_author, bg="#4CAF50", fg="white")
    submit_author_button.pack(pady=1)

    entry_label = tk.Label(search_books_win, text="Genre", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    genre_entry = tk.Entry(search_books_win, font=("David", 12), width=20)
    genre_entry.pack(pady=1)
    submit_genre_button = tk.Button(search_books_win, text="Submit", font=("David", 12),command=submit_genre, bg="#4CAF50", fg="white")
    submit_genre_button.pack(pady=1)

    entry_label = tk.Label(search_books_win, text="Year", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    year_entry = tk.Entry(search_books_win, font=("David", 12), width=20)
    year_entry.pack(pady=1)
    submit_year_button = tk.Button(search_books_win, text="Submit", font=("David", 12),command=submit_year, bg="#4CAF50", fg="white")
    submit_year_button.pack(pady=1)



    def back_to_main():
        search_books_win.destroy()
        Gui_menu.menu_window()  ##############################################

    back_button = tk.Button(search_books_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)


def view_search(results):

    view_search_win=tk.Toplevel()
    view_search_win.title("Search results")
    view_search_win.geometry("600x620")
    view_search_win.config(bg="#f0f0f0")
    entry_label = tk.Label(view_search_win, text="Search results", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)

    text_widget = tk.Text(view_search_win, font=("David", 12), height=32, width=80)
    text_widget.pack(pady=1)


    text_widget.delete(1.0, tk.END)
    i=1
    for item in results:
        text_widget.insert(tk.END, f"{i}. {item}\n")
        i+=1
    def back_to_main():
        view_search_win.destroy()
        Gui_menu.search_book_in_lib()

    back_button = tk.Button(view_search_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)

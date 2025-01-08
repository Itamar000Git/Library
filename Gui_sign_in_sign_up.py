import Gui_lib
import Gui_menu
from Gui_lib import *
from Gui_menu import *


def sign_up():
    Gui_lib.root.withdraw()
    second_win = tk.Toplevel()
    second_win.title("sign up")
    second_win.geometry("300x270")
    second_win.config(bg="#f0f0f0")

    entry_label = tk.Label(second_win, text="full name", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    name_entry = tk.Entry(second_win, font=("David", 12), width=20)
    name_entry.pack(pady=1)

    entry_label = tk.Label(second_win, text="age", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    age_entry = tk.Entry(second_win, font=("David", 12), width=20)
    age_entry.pack(pady=1)

    entry_label = tk.Label(second_win, text="user name", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    user_name_entry = tk.Entry(second_win, font=("David", 12), width=20)
    user_name_entry.pack(pady=1)

    entry_label = tk.Label(second_win, text="password", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    pass_entry = tk.Entry(second_win, font=("David", 12), width=20, show="*")
    pass_entry.pack(pady=1)
    new_user=[]
    def submit():   # after this function we can create user object
        try:
            user_input = name_entry.get()  # got ful name
            validate_non_empty_data(user_input)

            new_user.append(user_input)
            print(f"Entered full name: {user_input}")

            user_input = age_entry.get()  #got the age
            validate_non_empty_data(user_input)
            try:
                validate_input(int(user_input))
                new_user.append(user_input)
                print(f"Entered age: {user_input}")
            except:
                messagebox.showerror("Error", "Invalid age")
                second_win.destroy()
                sign_up()
                return

            user_input = user_name_entry.get()  #got the user name
            validate_non_empty_data(user_input)
            if not (check_user_name(user_input)):
                new_user.append(user_input)
                print(f"Entered user name: {user_input}")
            else:

                messagebox.showerror("Error", "Username already exists")
                second_win.destroy()
                sign_up()
                return

            user_input=pass_entry.get()
            validate_non_empty_data(user_input)
            user_input =hashlib.sha256(user_input.encode()).hexdigest()

            new_user.append(user_input)
            print(f"Entered password: {user_input}")
        except ValueError as e:
            messagebox.showerror("Error", e)
            second_win.destroy()
            sign_up()
            return

        if Librarian.create_librarian(new_user) is not None:
            messagebox.showinfo("Success", "User created successfully!\n Now need to sign in")
        back_to_main()
    new_user.clear()

    submit_button = tk.Button(second_win, text="Submit", font=("David", 12),command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        second_win.destroy()
        Gui_lib.root.deiconify()

    back_button = tk.Button(second_win, text="Back", font=("David", 12),command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)


def sign_in():

    Gui_lib.root.withdraw()
    second_win = tk.Tk()
    second_win.title("sign in")
    second_win.geometry("300x200")
    second_win.config(bg="#f0f0f0")

    entry_label = tk.Label(second_win, text="user name", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=5)

    user_name_entry = tk.Entry(second_win, font=("David", 12), width=20)
    user_name_entry.pack(pady=5)

    entry_label = tk.Label(second_win, text="password", font=("David", 12), bg="#f0f0f0")
    entry_label.pack(pady=5)

    password_entry = tk.Entry(second_win, font=("David", 12), width=20, show="*")
    password_entry.pack(pady=5)


    user_ditailes=[]
    def submit(): ## in the end of this function i need to hash the password and check if match

        user_input = user_name_entry.get()  # got username
        if check_user_name(user_input):
            user_ditailes.append(user_input)
            print(f"Entered user name: {user_input}")
        else:
            messagebox.showerror("Error", "Wrong username")
            second_win.destroy()
            sign_in()
            return

        user_input = hashlib.sha256(password_entry.get().encode()).hexdigest()  # got the password
        if (check_password(user_input, user_ditailes[0])):
            user_ditailes.append(user_input)
            print(f"Entered password: {user_input}")
        else:
            messagebox.showerror("Error", "Wrong password")
            second_win.destroy()
            sign_in()
            return

        user_ditailes.clear()
        second_win.destroy()
        Gui_menu.menu_window()

    submit_button = tk.Button(second_win, text="Submit", font=("David", 12),command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        second_win.destroy()
        Gui_lib.root.deiconify()

    back_button = tk.Button(second_win, text="Back", font=("David", 12), command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)





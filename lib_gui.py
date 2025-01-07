import tkinter as tk

def second_window(choice):
    if choice == "sign in":
        sign_in()
    elif choice == "sign up":
        sigh_up()

def sigh_up():
    root.destroy()
    second_win = tk.Tk()
    second_win.title("sign up")
    second_win.geometry("300x270")
    second_win.config(bg="#f0f0f0")

    entry_label = tk.Label(second_win, text="full name", font=("Arial", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    entry = tk.Entry(second_win, font=("Arial", 12), width=20)
    entry.pack(pady=1)

    entry_label = tk.Label(second_win, text="age", font=("Arial", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    entry1 = tk.Entry(second_win, font=("Arial", 12), width=20)
    entry1.pack(pady=1)

    entry_label = tk.Label(second_win, text="user name", font=("Arial", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    entry2 = tk.Entry(second_win, font=("Arial", 12), width=20)
    entry2.pack(pady=1)

    entry_label = tk.Label(second_win, text="password", font=("Arial", 12), bg="#f0f0f0")
    entry_label.pack(pady=1)
    entry3 = tk.Entry(second_win, font=("Arial", 12), width=20, show="*")
    entry3.pack(pady=1)

    def submit():   # after this function we can create user object
        user_input = entry.get()  ################################################## got ful name
        print(f"Entered full name: {user_input}")
        tk.Label(second_win, text="", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        user_input = entry1.get()  ####################################################got the age
        print(f"Entered age: {user_input}")
        tk.Label(second_win, text="", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        user_input = entry2.get()  ####################################################got the user name
        print(f"Entered user name: {user_input}")
        tk.Label(second_win, text="", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        user_input = entry3.get()  ####################################################got the password
        print(f"Entered password: {user_input}")
        tk.Label(second_win, text="", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

    submit_button = tk.Button(second_win, text="Submit", font=("Arial", 12),command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=1)

    def back_to_main():
        second_win.destroy()





    back_button = tk.Button(second_win, text="Back", font=("Arial", 12),
                             command=back_to_main, bg="#FFA500", fg="white")
    back_button.pack(pady=1)


def sign_in():

    root.destroy()
    second_win = tk.Tk()
    second_win.title("sign in")
    second_win.geometry("300x200")
    second_win.config(bg="#f0f0f0")
    entry_label = tk.Label(second_win, text="user name", font=("Arial", 12), bg="#f0f0f0")
    entry_label.pack(pady=5)

    entry = tk.Entry(second_win, font=("Arial", 12), width=20)
    entry.pack(pady=5)

    entry_label = tk.Label(second_win, text="password", font=("Arial", 12), bg="#f0f0f0")
    entry_label.pack(pady=5)

    entry1 = tk.Entry(second_win, font=("Arial", 12), width=20, show="*")
    entry1.pack(pady=5)



    def submit(): ## in the end of this function i need to hash the password and check if match
        user_input = entry.get() ################################################## got username
        print(f"Entered user name: {user_input}")
        tk.Label(second_win, text="", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)
        user_input = entry1.get()####################################################got the password
        print(f"Entered password: {user_input}")
        tk.Label(second_win, text="Password received!", font=("Arial", 12), bg="#f0f0f0").pack(pady=10)

    submit_button = tk.Button(second_win, text="Submit", font=("Arial", 12),
                              command=submit, bg="#4CAF50", fg="white")
    submit_button.pack(pady=10)






def on_button_click(button_text):
    print(button_text)
    second_window(button_text)




if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    root.title("Library")
    root.geometry("300x200")  # Set the size of the window
    root.config(bg="#2d2d2d")

    display = tk.StringVar()  # A StringVar to manage the content of the display (entry field)

    buttons = [
        ('sign in', 3, 2),
        ('sign up', 3, 3)  # Add a clear button at the bottom
    ]


    for (text, row, col) in buttons:
        button = tk.Button(root, text=text, font=("David", 20), height=1, width=6,  # Create a button with the specified text and appearance
                           command=lambda t=text: on_button_click(t),  # Assign the on_button_click function to the button
                           bg="#4CAF50", fg="white")  # Set the button colors
        button.grid(row=row, column=col, padx=3, pady=3)  # Place the button in the correct grid position

    # Configure row and column lengths to make the calculator responsive
    for i in range(0,6):  # Iterate over all rows and columns in the grid
        if i != 0:
          root.grid_rowconfigure(i, weight=1)  # Assign a weight to each row to make them resizable
        root.grid_columnconfigure(i, weight=1)  # Assign a weight to each column to make them resizable



    root.mainloop()
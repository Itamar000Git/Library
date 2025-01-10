import hashlib
import tkinter as tk
from tkinter import messagebox
from Gui_menu import *
import main
from Gui_sign_in_sign_up import *
from Librarian import *

# support exit button for exit all program
def exit():
    root.destroy()
   # exit()

def second_window(choice):
    if choice == "sign in":
        sign_in()
    elif choice == "sign up":
        sign_up()


# def on_button_click(button_text):###########################################
#     print(button_text)
#     second_window(button_text)


'''
This is the main gui function that starts all gui program.
The first window is ths sign in , sigh up and exit buttons'''
def maingui():
    root.title("Library")
    root.geometry("300x200")  # Set the size of the window
    root.config(bg="#2d2d2d")

    sign_in_but=tk.Button(root, text="sign in", font=("David", 20), height=1, width=6,command=lambda t="sign in": second_window(t), bg="#4CAF50", fg="white")
    sign_in_but.pack(pady=5)

    sign_up_but = tk.Button(root, text="sign up", font=("David", 20), height=1, width=6,command=lambda t="sign up": second_window(t), bg="#4CAF50", fg="white")
    sign_up_but.pack(pady=5)


    exit_but = tk.Button(root, text="exit", font=("David", 12), height=1, width=6,command=exit, bg="#FF0000", fg="white")
    exit_but.pack(pady=5)


    root.mainloop()

root = tk.Tk()
if __name__ == "__main__":
    maingui()


import tkinter as tk
from tkinter import messagebox


def login():
    messagebox.showinfo("Login", "Login success!")


def some_action():
    message = text_enter.get()
    if message:
        # messagebox.showinfo("Action", f"Custom action performed with text: {message}")
        show_input_text(message)
    else:
        messagebox.showwarning("Action", "Please enter text first.")


def show_input_text(text):
    messagebox.showinfo("Function", f"The text you entered was: {text}")


root_window = tk.Tk()
root_window.title("Application screen")
root_window.geometry("350x200")
root_window.configure(borderwidth=3)

label_login = tk.Label(root_window, text="Login to Page XXX")
label_login.pack()

btn_login = tk.Button(root_window, text="Login", command=login)
btn_login.pack()

spacing = tk.Label(root_window, text="")
spacing.pack()

label_text = tk.Label(root_window, text="Please, type a text:")
label_text.pack()

text_enter = tk.Entry(root_window)
text_enter.pack()

btn_action = tk.Button(root_window, text="Perform the custom action", command=some_action)
btn_action.pack()

root_window.mainloop()

from tkinter import *


root = Tk()
colors = ["blue", "red", "green", "purple", "orange"]
current_color_index = 0

username = Entry(root, borderwidth=3)
username.grid(row=0, column=1)

def after_btn_click_me():
    global current_color_index
    next_color = colors[current_color_index]

    text = f"{username.get()}, u clicked on meee!!"
    label = Label(root, text=text, fg=next_color)
    label.grid(row=2, column=1)

    current_color_index = (current_color_index + 1) % len(colors)

label_name = Label(root, text="Hey, what is your name?")
label_name.grid(row=0, column=0)

label_play = Label(root, text="Let's play")
label_play.grid(row=1, column=0)

button_disable = Button(root, text="Disabled :(", state=DISABLED)
button_disable.grid(row=3, column=0)
button_click_me = Button(root, text="Click on meee!", padx=50,
                         pady=10, command=after_btn_click_me,
                         bg="pink")
button_click_me.grid(row=1, column=1)

root.mainloop()

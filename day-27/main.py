from tkinter import *


def button_clicked():
    new_text = user_input.get()
    label_1.config(text=new_text)


# Window
window = Tk()
window.title("Look Ma, I made a Window!")
window.minsize(width=500, height=300)
window.config(padx=10, pady=10)

# Label
label_1 = Label(text="Look at MEEEE!", font=("Arial", 36, "italic"))
label_1.grid(column=0, row=0)
# label_1["text"] = "I'm still doing it!"
label_1.config(padx=20, pady=20)


# Button
button = Button(text="Click me!", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="What about Me?", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
user_input.grid(column=3, row=2)

window.mainloop()

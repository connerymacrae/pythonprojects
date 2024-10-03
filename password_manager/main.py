from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_nums = [choice(numbers) for _ in range(randint(2, 14))]

    pass_list = pass_letters + pass_symbols + pass_nums
    shuffle(pass_list)
    password = ''.join(pass_list)

    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Hold Up!", message="You've got some empty fields pardner!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered:\nEmail: {email}\n"
                                       f"Password: {password}\nWould you like to save?")
        if is_ok:
            with open("data.txt", "a+") as pass_file:
                pass_file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, 'end')
                password_input.delete(0, 'end')
                website_input.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# logo image and canvas
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200,)
canvas_img = canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# labels and entries
website_label = Label(text="Website:",)
website_label.grid(row=1, column=0)

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2)
# place cursor in website input field
website_input.focus()

email_label = Label(text=f"Email/Username:")
email_label.grid(row=2, column=0)

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2)
# email input default
email_input.insert(0, "macrae.connery@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_input = Entry(width=19)
password_input.grid(row=3, column=1)

# buttons
generate_pass_button = Button(text="Generate Password", width=12, command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add Password", width=33, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()

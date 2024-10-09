from tkinter import *
import pandas
from random import choice


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
language_dict = {}

try:
    data = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    original_data = pandas.read_csv('data/gaelic_flash.csv')
    language_dict = original_data.to_dict(orient="records")
else:
    language_dict = data.to_dict(orient="records")


def new_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(language_dict)
    canvas.itemconfig(language_text, text="Gaelic", fill="black")
    canvas.itemconfig(word_text, text=current_card['Gaelic'], fill="black")
    canvas.itemconfig(canvas_img, image=card_front_img)
    flip_timer = window.after(5000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(language_text, text="English", fill='white')
    canvas.itemconfig(word_text, text=current_card['English'], fill='white')


def press_check():
    language_dict.remove(current_card)
    words_to_learn = pandas.DataFrame(language_dict)
    words_to_learn.to_csv('data/words_to_learn.csv', index=False)
    new_card()

    # try:
    #     data = pandas.read_csv('data/words_to_learn.csv')
    # except FileNotFoundError:
    #     data = pandas.read_csv('data/short_sheet.csv')
    # finally:
    #     language_dict = data.to_dict(orient="records")


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(4000, func=flip_card)

card_back_img = PhotoImage(file="images/card_back.png")
card_front_img = PhotoImage(file="images/card_front.png")
check_img = PhotoImage(file="images/right.png")
x_img = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas.create_image(400, 263, image=card_front_img)
language_text = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

x_button = Button(image=x_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=new_card)
x_button.grid(row=1, column=0)

check_button = Button(image=check_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=press_check)
check_button.grid(row=1, column=1)

new_card()

window.mainloop()

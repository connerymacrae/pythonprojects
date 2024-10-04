from tkinter import *
import math
from playsound3 import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT = ('Courier', 56, "bold")
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = "None"
ding_sound = "ding.mp3"
bark_sound = "bark.mp3"
big_bell_sound = "big_bell.mp3"


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"00:00")
    canvas.itemconfig(canvas_img, image=doge_img)
    timer_label.config(text="TIMER")
    check_marks.config(text="")
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        timer_label.config(text="BREAAAAK!", fg=PINK)
        canvas.itemconfig(canvas_img, image=doge_long_break_img)
        playsound(big_bell_sound)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break', fg=YELLOW)
        canvas.itemconfig(canvas_img, image=doge_break_img)
        playsound(bark_sound)
    else:
        count_down(work_sec)
        timer_label.config(text='work.', fg=RED)
        canvas.itemconfig(canvas_img, image=doge_img)
        playsound(ding_sound)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    # global reps

    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✓"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Doge Watch You Work Pomodoro Timer")
window.config(padx=60, pady=20, bg=GREEN)

doge_long_break_img = PhotoImage(file="long_break_shiba.png")
doge_break_img = PhotoImage(file="doge_break.png")
doge_img = PhotoImage(file="doge.png")
canvas = Canvas(width=512, height=512, bg=GREEN, highlightthickness=0)
canvas_img = canvas.create_image(256, 256, image=doge_img)
timer_text = canvas.create_text(180, 300, text="00:00", fill=RED, font=FONT)
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", font=FONT, fg=RED, bg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="START", highlightbackground=GREEN, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", highlightbackground=GREEN, command=reset_timer)
reset_button.grid(column=2, row=2)

check_marks = Label(text="", font=FONT, fg=RED, bg=GREEN)
check_marks.grid(column=1, row=3)
check_marks.config(pady=40)

window.mainloop()

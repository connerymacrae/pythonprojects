from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
# TRUE_IMG = PhotoImage(file="images/true.png")
# FALSE_IMG = PhotoImage(file="images/false.png")

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_image = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.score_label = Label(text=f"Score: Current Score", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Question Text",
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=20)

        self.true_button = Button(image=true_image, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.true_button.grid(row=2, column=1, pady=20)

        self.false_button = Button(image=false_img, highlightthickness=0, highlightbackground=THEME_COLOR)
        self.false_button.grid(row=2, column=0, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

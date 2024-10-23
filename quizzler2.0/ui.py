from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        true_image = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")

        self.score_label = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
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

        self.true_button = Button(image=true_image, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.guess_true)
        self.true_button.grid(row=2, column=1, pady=20)

        self.false_button = Button(image=false_img, highlightthickness=0, highlightbackground=THEME_COLOR, command=self.guess_false)
        self.false_button.grid(row=2, column=0, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"Quiz Complete!\nFinal Score: {self.quiz.score}/{len(self.quiz.question_list)}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def guess_true(self):
        self.give_feedback(self.quiz.check_answer("True"))
        # user_guess = "True"
        # if self.quiz.check_answer(user_guess):
        #     self.canvas.config(bg="green")
        #     self.score_label.config(f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
        # else:
        #     self.canvas.config(bg="red")
        # # self.score_label.config(text=f"Score: {current_score}/{len(self.quiz.question_list)}")
        # self.window.after(1000, func=self.get_next_question)



    def guess_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)
        # user_guess = "False"
        # if self.quiz.check_answer(user_guess):
        #     self.canvas.config(bg="green")
        #     self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")
        # else:
        #     self.canvas.config(bg="red")
        # # self.score_label.config(text=f"Score: {current_score}/{len(self.quiz.question_list)}")
        # self.window.after(1000, func=self.get_next_question)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)

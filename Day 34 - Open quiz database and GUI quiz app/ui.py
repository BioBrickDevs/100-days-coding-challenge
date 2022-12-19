import tkinter as tk
import os
import quiz_brain
IMAGE_DIRECTORY_PATH = os.getcwd() + "/images/"
THEME_COLOR = "#375362"


class QuizGUI(object):
    def __init__(self, object: quiz_brain.QuizBrain):
        self.quiz = object
        self.window = tk.Tk()
        self.window.title("Tkinter Quiz App")
        # self.window.geometry("300x300")
        self.window.config(background=THEME_COLOR, padx=20, pady=20)
        self.canvas = tk.Canvas(background="white", height=250, width=300)
        self.canvas.grid(row=1, column=0, columnspan=2)
        self.content_text = self.canvas.create_text(150, 125, text="Hello",
                                                    font=("Arial", 15, "italic",), width=200)
        self.score_text = tk.Label(text="Score: 0", padx=20, pady=20,
                                   background=THEME_COLOR, foreground="white")
        self.score_text.grid(row=0, column=1)

        self.right_button_image = tk.PhotoImage(
            file=IMAGE_DIRECTORY_PATH + "true.png",)
        self.wrong_button_image = tk.PhotoImage(
            file=IMAGE_DIRECTORY_PATH + "false.png")

        self.right_button = tk.Button(
            image=self.right_button_image, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(row=2, column=1, pady=40)
        self.wrong_button = tk.Button(
            image=self.wrong_button_image, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(row=2, column=0, pady=40)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():

            self.score_text.config(text=f"Score: {self.quiz.score}")
            next_question = self.quiz.next_question()
            self.canvas.itemconfig(self.content_text, text=next_question)
        else:
            self.canvas.itemconfig(
                self.content_text, text="You have completed the quiz!")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def true_pressed(self):
        if self.quiz.still_has_questions():
            is_right = self.quiz.check_answer("True")

            self.feedback_to_user_display(is_right)

    def false_pressed(self):
        if self.quiz.still_has_questions():
            is_right = self.quiz.check_answer("False")
            self.feedback_to_user_display(is_right)

    def feedback_to_user_display(self, answer: bool):
        if answer:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")

        self.window.after(1000, self.next_question)

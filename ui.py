THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score:0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="text",
                                                     width=280,
                                                     fill=THEME_COLOR,
                                                     font=("Ariel", 15, "italic")
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        true_img = PhotoImage(file="images/true.png")
        self.green_button = Button(image=true_img, highlightthickness=0, command=self.true)
        self.green_button.grid(row=2, column=0)

        false_img = PhotoImage(file="images/false.png")
        self.red_button = Button(image=false_img, highlightthickness=0, command=self.false)
        self.red_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.green_button.config(state="disabled")
            self.red_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="fin")

    def true(self):
        is_right = self.quiz.check_answer("True")
        self.feedback(is_right)
        #self.get_next_question()

    def false(self):
        self.feedback(self.quiz.check_answer("False"))
        #self.get_next_question()

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


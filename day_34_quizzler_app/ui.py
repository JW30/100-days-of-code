import os.path
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT_SCORE = ("Arial", 16, "normal")
FONT_QUESTION = ("Arial", 20, "italic")


class TriviaUI(Tk):

    def __init__(self, quiz: QuizBrain):
        super().__init__()
        self.quiz: QuizBrain = quiz

        # Main Window
        self.title("Quizzler")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(10, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(10, weight=1)
        self.config(pady=20, padx=20, bg=THEME_COLOR)

        # Label
        self.score_label: Label = Label(text=f"Score: 0/{len(self.quiz.question_list)}", font=FONT_SCORE,
                                        bg=THEME_COLOR)
        self.score_label.grid(row=1, column=2)

        # Canvas
        self.canvas: Canvas = Canvas(bg="white", highlightbackground=THEME_COLOR, width=300, height=250)
        self.question_text: int = self.canvas.create_text(150, 125, justify="center", text="", fill="black",
                                                          font=FONT_QUESTION, width=250)
        self.canvas.grid(row=2, column=1, columnspan=2, sticky=W + E, pady=50)

        # Buttons
        self.true_img: PhotoImage = PhotoImage(file=os.path.join("images", "true.png"))
        self.true_btn: Button = Button(image=self.true_img, highlightbackground=THEME_COLOR, command=self.true_pressed)
        self.true_btn.grid(row=3, column=1)

        self.false_img: PhotoImage = PhotoImage(file=os.path.join("images", "false.png"))
        self.false_btn: Button = Button(image=self.false_img, highlightbackground=THEME_COLOR,
                                        command=self.false_pressed)
        self.false_btn.grid(row=3, column=2)

        self.switch_buttons()
        self.get_next_question()

        self.mainloop()

    def switch_buttons(self) -> None:
        if self.true_btn.cget("state") == NORMAL:
            self.true_btn.config(state=DISABLED)
            self.false_btn.config(state=DISABLED)
        else:
            self.true_btn.config(state=NORMAL)
            self.false_btn.config(state=NORMAL)

    def finish_game(self) -> None:
        self.canvas.itemconfig(self.question_text, text="Congratulations!\n\nYou have finished the quiz :)")

    def update_score(self) -> None:
        self.quiz.score += 1
        self.score_label.config(text=f"Score: {self.quiz.score}/{len(self.quiz.question_list)}")

    def give_feedback(self, is_right: bool) -> None:
        self.switch_buttons()
        if is_right:
            self.canvas.config(bg="green")
            self.update_score()
        else:
            self.canvas.config(bg="red")
        self.after(1000, self.get_next_question)

    def true_pressed(self) -> None:
        is_right = self.quiz.current_question.answer == "True"
        self.give_feedback(is_right)

    def false_pressed(self) -> None:
        is_right = self.quiz.current_question.answer == "Wrong"
        self.give_feedback(is_right)

    def get_next_question(self) -> None:
        self.switch_buttons()
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.switch_buttons()
            self.finish_game()

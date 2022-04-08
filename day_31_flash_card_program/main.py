from tkinter import *
import pandas as pd
import os
import random

BACKGROUND_COLOR: str = "#B1DDC6"
FONT_LANGUAGE: tuple = ("Arial", 40, "italic")
FONT_WORD: tuple = ("Arial", 60, "bold")

ALL_WORDS_PATH = os.path.join("data", "french_words.csv")
REMAINING_PATH = os.path.join("data", "words_to_learn.csv")
DATA_PATH = REMAINING_PATH if os.path.exists(REMAINING_PATH) else ALL_WORDS_PATH
DATA: pd.DataFrame = pd.read_csv(DATA_PATH)


class FlashcardApp(Tk):

    def __init__(self) -> None:
        super().__init__()
        self.remaining_cards: list = DATA.to_dict(orient="records")
        self.current_card: dict = {}

        # Main Window
        self.title("Flashy")
        self.rowconfigure(0, weight=1)
        self.rowconfigure(3, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(3, weight=1)
        self.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

        # Canvas
        self.canvas: Canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.card_front_img: PhotoImage = PhotoImage(file=os.path.join("images", "card_front.png"))
        self.card_back_img: PhotoImage = PhotoImage(file=os.path.join("images", "card_back.png"))
        self.canvas_img: int = self.canvas.create_image(400, 263, image=self.card_front_img)
        self.language: int = self.canvas.create_text(400, 150, fill="black", font=FONT_LANGUAGE)
        self.word: int = self.canvas.create_text(400, 263, fill="black", font=FONT_WORD)
        self.canvas.grid(row=1, column=1, columnspan=2, sticky=W+E)

        # Buttons
        self.yes_img: PhotoImage = PhotoImage(file=os.path.join("images", "right.png"))
        self.yes_btn: Button = Button(image=self.yes_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                                      command=self.remove_and_next)
        self.yes_btn.grid(row=2, column=1)

        self.no_img: PhotoImage = PhotoImage(file=os.path.join("images", "wrong.png"))
        self.no_btn: Button = Button(image=self.no_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR,
                                     command=self.next_card)
        self.no_btn.grid(row=2, column=2)

        # Start application
        self.flip_timer: str = self.after(1, func=self.next_card)

    # Logic
    def save_progress(self) -> None:
        df = pd.DataFrame(self.remaining_cards)
        df.to_csv(REMAINING_PATH, index=False)

    def show_congrats(self) -> None:
        self.after_cancel(self.flip_timer)
        self.canvas.itemconfig(self.canvas_img, image=self.card_front_img)
        self.canvas.itemconfig(self.language, text="Congratulations!", fill="black")
        self.canvas.itemconfig(self.word, text="Flashcards empty! :)", fill="black")
        self.yes_btn.destroy()
        self.no_btn.destroy()

    def remove_and_next(self) -> None:
        self.remaining_cards.remove(self.current_card)
        self.save_progress()
        if self.remaining_cards:
            self.next_card()
        else:
            os.remove(REMAINING_PATH)
            self.show_congrats()

    def flip_card(self) -> None:
        self.canvas.itemconfig(self.canvas_img, image=self.card_back_img)
        self.canvas.itemconfig(self.language, text="English", fill="white")
        self.canvas.itemconfig(self.word, text=self.current_card["English"], fill="white")

    def next_card(self) -> None:
        self.after_cancel(self.flip_timer)
        self.current_card: dict = random.choice(self.remaining_cards)
        self.canvas.itemconfig(self.canvas_img, image=self.card_front_img)
        self.canvas.itemconfig(self.language, text="French", fill="black")
        self.canvas.itemconfig(self.word, text=self.current_card["French"], fill="black")
        self.flip_timer = self.after(3000, func=self.flip_card)


if __name__ == "__main__":
    app = FlashcardApp()
    app.mainloop()
from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def  is_known():
    to_learn.remove(current_card)
    data1 = pandas.DataFrame(to_learn)
    data1.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_bg, image=back_image)
    canvas.itemconfig(language, text="English", fill="white")
    canvas.itemconfig(translation, text=current_card["English"], fill="white")

def next_card():
    global current_card, timer
    timer = window.after_cancel(timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(language, text="French", fill="black")
    canvas.itemconfig(translation, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=front_image)
    timer = window.after(3000, func=flip_card)


window = Tk()
window.title("French To English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


front_image = PhotoImage(file="./images/card_front.png")
back_image = PhotoImage(file="./images/card_back.png")
right_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")

timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_bg = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT)
translation = canvas.create_text(400, 263, text="Word", font=WORD_FONT)
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


next_card()



window.mainloop()

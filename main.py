BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"

from tkinter import *
import pandas
from tkinter import messagebox
import random
import pyperclip
import json













window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

canvas = Canvas(width=800, height=562, highlightthickness=0, bg=BACKGROUND_COLOR)
card_back = PhotoImage(file="./images/card_back.png")
canvas.create_image(400, 263, image=card_back)
canvas.grid(column=0, row=0, columnspan=2)

title = canvas.create_text(400, 150, text="Title", font=(FONT, 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=(FONT, 60, "bold"))

right_img = PhotoImage(file="./images/right.png")
right = Button(image=right_img, highlightthickness=0)
right.grid(column=1, row=1)

wrong_img = PhotoImage(file="./images/wrong.png")
wrong = Button(image=wrong_img, highlightthickness=0)
wrong.grid(column=0, row=1)


















window.mainloop()
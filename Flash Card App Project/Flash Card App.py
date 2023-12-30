from tkinter import *
import pandas as pd
import random as rd

BACKGROUND_COLOR = "#B1DDC6"
# For the card can show the state of current word when click know or unknow button
current_card = {}

# Try to learned word file, if file is exist that will read it.
try:
    data = pd.read_csv("data/words_to_learn.csv")
# If file doen't exist will read the data from original file
except FileNotFoundError:
    original_data = pd.read_csv("data/English Frequently list to Thai.csv")
    # oreient is set a dict from data fram as column=key and row=value
    to_learn = original_data.to_dict(orient="records")
    num_word = len(original_data)-1
# If file is exist, so create a dataframe
else:
    to_learn = data.to_dict(orient="records")
    num_word = len(to_learn)-1

# After click known or unknow button, will generate a net card
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = rd.choice(to_learn)
    canvas.itemconfig(card_title, text="English", fill="black")
    canvas.itemconfig(card_word, text=current_card["English"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)
    
# If not known the word will flip after 3 second
def flip_card():
    canvas.itemconfig(card_title, text="Thai", fill="white")
    canvas.itemconfig(card_word, text=current_card["Thai"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
 
# IF know the word click the know button to next card
# And remove the known word from current_card   
def is_known():
    # remove learned word from original data
    to_learn.remove(current_card)
    remain_word = len(to_learn)-1
    canvas.itemconfig(card_remain, text=f"Remaining {remain_word} words",font=("Ariel", 30, "italic"))
    # Create a DataFrame and updatea a learned word
    data = pd.DataFrame(to_learn)
    # index=False for adding a data without index column of csv file
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

window = Tk()
window.title("Flash Card : Learn English word",)
window.config(padx=50,pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Set import img size
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_img)
card_remain = canvas.create_text(400,100, text=f"Remaning {num_word} words",font=("Ariel", 30, "italic"))
card_title = canvas.create_text(400, 200, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)
next_card()


window.mainloop()

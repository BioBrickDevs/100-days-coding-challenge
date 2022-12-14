import tkinter as tk
import tkinter.messagebox
import os
import pandas
import random
import json

PATH = os.getcwd() + "/images/"
PATH_NEW_JSON = os.getcwd() + "/data/data.json"
PATH_ORIGINAL_CSV = os.getcwd() + "/data/french_words.csv"
timer = None
tk_after_id = None
random_key = None
data = None
 

def load_data():
    global data
    try:
        with open(PATH_NEW_JSON, "r") as file:
            data = json.load(file)
            print(data)
    except:
        with open(PATH_ORIGINAL_CSV, "r") as data_file:
            data = pandas.read_csv(data_file)
            global window
            data = data.to_dict()


def save_data():
    print("Saved data")
    try:
        with open(PATH_NEW_JSON, "r") as file:
            data_this_loop = json.load(file)

        with open(PATH_NEW_JSON, "w") as file:
            data_this_loop = data_this_loop.update(data)
            json.dump(data_this_loop, file)
    except:
        with open(PATH_NEW_JSON, "w") as file:
            json.dump(data, file)


def delete():
    global window, tk_after_id
    if tk_after_id:
        window.after_cancel(tk_after_id)
    global random_key
    global data
    try:
        del data["French"][random_key]
        del data["English"][random_key]
        generate_french_word()
        save_data()
    except:
        tkinter.messagebox.showinfo(
            message="All cards have been learned try to add new ones!.")


def generate_french_word():
    global tk_after_id
    global window
    if tk_after_id:
        window.after_cancel(tk_after_id)
    global random_key
    canvas.itemconfig(canvas_image, image=img_card_front)
    global data

    try:
        # iterate over the dict items
        choices = [k for k, v in data["French"].items()]

        random_number = random.choice(choices)
        random_key = random_number

        random_french_word = data["French"][random_key]
        canvas.itemconfigure(word_text, text=random_french_word, fill="black")
        canvas.itemconfigure(language_text, text="French", fill="black")
    except:
        tkinter.messagebox.showinfo(
            message="All the cards have been marked to learned try new ones.")
    tk_after_id = window.after(3000, english_word)
    # english_word(random_key)


def english_word():
    global random_key
    global window
    global tk_after_id
    window.after_cancel(tk_after_id)
    global path_to_data
    global data
    random_english_word = data["English"][random_key]
    canvas.itemconfigure(word_text, text=random_english_word, fill="white")
    canvas.itemconfigure(language_text, text="English", fill="white")
    canvas.itemconfig(canvas_image, image=img_card_back)


BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.configure(padx=50, pady=50, width=900, height=626, bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)


img_card_front = tk.PhotoImage(file=PATH+"card_front.png")

img_card_back = tk.PhotoImage(file=PATH+"card_back.png")
img_right = tk.PhotoImage(file=PATH + "right.png")
canvas_image = canvas.create_image(400, 263, image=img_card_front)

language_text = canvas.create_text(400, 150, text="French", font=(
    "Ariel", 30, "italic"), fill="black")
word_text = canvas.create_text(
    400, 263, text="Yes", font=("Ariel", 60, "bold"), fill="black")

canvas.grid(row=0, column=0, columnspan=2)


button_right = tk.Button(
    image=img_right, highlightthickness=0, command=delete)
button_right.grid(column=1, row=1)
img_wrong = tk.PhotoImage(file=PATH+"wrong.png")
button_wrong = tk.Button(
    image=img_wrong, highlightthickness=0, command=generate_french_word)
button_wrong.grid(column=0, row=1)
load_data()
generate_french_word()

window.mainloop()

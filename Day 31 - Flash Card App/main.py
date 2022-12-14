import tkinter as tk
import tkinter.messagebox
import os
import pandas
import random


path = os.getcwd() + "/images/"
print(path)
timer = None
path_to_data = os.getcwd() + "/data/french_words.csv"
tk_after_id = None
random_key = None

with open(path_to_data) as data_file:
    data = pandas.read_csv(data_file)
    global window
    data = data.to_dict()

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
    except:
        tkinter.messagebox.showinfo(message="All cards have been learned try to add new ones!.")
def generate_french_word():
    global tk_after_id
    global window
    if tk_after_id:
        window.after_cancel(tk_after_id)
    global random_key
    canvas.itemconfig(canvas_image,image=img_card_front)
    global data
    
    try:
        choices = [k for k, v in data["French"].items()] # iterate over the dict items
        
        random_number = random.choice(choices)
        random_key = random_number
    
        random_french_word = data["French"][random_key]
        canvas.itemconfigure(word_text, text=random_french_word, fill="black")
        canvas.itemconfigure(language_text, text="French", fill="black")
    except:
        tkinter.messagebox.showinfo(message="All the cards have been marked to learned try new ones.")
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
    canvas.itemconfig(canvas_image,image=img_card_back)

BACKGROUND_COLOR = "#B1DDC6"

window = tk.Tk()
window.configure(padx=50, pady=50, width=900, height=626, bg=BACKGROUND_COLOR)
canvas = tk.Canvas(width=800, height=526, bg=BACKGROUND_COLOR)


img_card_front = tk.PhotoImage(file=path+"card_front.png")

img_card_back = tk.PhotoImage(file=path+"card_back.png")
img_right = tk.PhotoImage(file=path + "right.png")
canvas_image  =canvas.create_image(400, 263, image=img_card_front)

language_text = canvas.create_text(400, 150, text="French", font=(
    "Ariel", 30, "italic"), fill="black")
word_text = canvas.create_text(
    400, 263, text="Yes", font=("Ariel", 60, "bold"), fill="black")

canvas.grid(row=0, column=0, columnspan=2)


button_right = tk.Button(
    image=img_right, highlightthickness=0, command=delete)
button_right.grid(column=1, row=1)
img_wrong = tk.PhotoImage(file=path+"wrong.png")
button_wrong = tk.Button(
    image=img_wrong, highlightthickness=0, command=generate_french_word)
button_wrong.grid(column=0, row=1)

generate_french_word()

window.mainloop()

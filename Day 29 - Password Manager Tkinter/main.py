import tkinter
import os
import tkinter.messagebox

import random


directory_path = os.getcwd()
print("My current directory is : " + directory_path)
filepath = directory_path + "/logo2.gif"
print(filepath)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    password_field.delete(0,tkinter.END)
    password_field.insert(0,password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data_to_file():

    website = website_field.get()
    email_usr = email_user_field.get()
    password = password_field.get()

    input = tkinter.messagebox.askokcancel(
        f"Are you sure you want to save this information? {website}, {email_usr}, {password}",
        f"Are you sure you want to save this information? {website}, {email_usr}, {password}")

    if input:

        with open(file="./data.txt", mode="a") as file:
            file.write(f"{website}|{email_usr}|{password}\n")

        password_field.delete(0, tkinter.END)
        website_field.delete(0, tkinter.END)
        email_user_field.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #
# image_path =
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
image_file = tkinter.PhotoImage(file=filepath)
canvas = tkinter.Canvas(window, height=200, width=200,
                        bg="white", highlightthickness=0)

canvas.grid(column=1, row=0)
canvas.create_image(100, 100, image=image_file)


wehsite_txt = tkinter.Label(text="Website:")
wehsite_txt.grid(column=0, row=1)
email_usr_txt = tkinter.Label(text="Email/Username:")
email_usr_txt.grid(column=0, row=2)
password_txt = tkinter.Label(text="Password:")
password_txt.grid(column=0, row=3)

gen_pswd_button = tkinter.Button(
    text="Generate Password", command=generate_password)
gen_pswd_button.grid(column=2, row=3)

add_button = tkinter.Button(text="Add", width=55, command=save_data_to_file)
add_button.grid(column=1, row=4, columnspan=2)

website_field = tkinter.Entry(text="a", width=55)
website_field.insert(0, "")
website_field.grid(column=1, row=1, columnspan=2)

password_field = tkinter.Entry(text="b", width=33)
password_field.insert(0, "")
password_field.grid(column=1, row=3, columnspan=1)


email_user_field = tkinter.Entry(text="c", width=55)
email_user_field.insert(0, "")
email_user_field.grid(column=1, row=2, columnspan=2)


window.mainloop()

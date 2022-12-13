import tkinter
import os


path_to_dir = os.path.abspath(__file__)

print(path_to_dir)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# image_path =


window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")
image_file = tkinter.PhotoImage(
    file="/home/biobbrick/100 days coding challenge/Day 29 - Password Manager Tkinter/logo2.gif")
canvas = tkinter.Canvas(window, height=200, width=200, bg="white", highlightthickness=0)
 
canvas.grid(column= 1,row = 0)
canvas.create_image(100, 100, image=image_file)


wehsite_txt = tkinter.Label(text="Website:")
wehsite_txt.grid(column =0,row=1)
email_usr_txt = tkinter.Label(text="Email/Username:")
email_usr_txt.grid(column=0,row=2)
password_txt = tkinter.Label(text="Password:")
password_txt.grid(column=0, row=3)

gen_pswd_button  =tkinter.Button(text = "Generate Password")
gen_pswd_button.grid(column=2,row=3)

add_button= tkinter.Button(text = "Add", width=55)
add_button.grid(column=1, row=4, columnspan=2)

website_field = tkinter.Entry( text= "website", width=55 )
website_field.insert(0, "Website")
website_field.grid(column= 1, row =1, columnspan= 2)

password_field = tkinter.Entry(text="pwd" ,width=33)
password_field.insert(0, "pwd")
password_field.grid(column = 1, row = 3,columnspan=1)


email_user_field = tkinter.Entry(width=55)
email_user_field.insert(0, "user/email")
email_user_field.grid(column=1, row=2,columnspan=2)



window.mainloop()

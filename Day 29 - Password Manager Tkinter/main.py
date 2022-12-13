import tkinter






# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
image_file = tkinter.PhotoImage(file="logo.png")
canvas = tkinter.Canvas(window, height=100, width=100)

canvas.pack()
canvas.create_image(100,100, image=image_file)

window.mainloop()
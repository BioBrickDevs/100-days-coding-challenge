import tkinter
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count_down():
    global reps
    global timer
    reps += 1
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        mode.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:

        str = ""
        marks = int(reps / 2)
        if reps % 2 == 0:
            for rep in range(marks):

                str += "✅"

        check_marks.config(text=str, bg=YELLOW, fg=GREEN, font=(35))
        count_down(short_break)
        mode.config(text="Short Break", fg=PINK)
    else:
        mode.config(text="Work", fg=GREEN)
        count_down(WORK_MIN * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(seconds):
    global reps
    global timer
    count_min = math.floor(seconds / 60)
    count_sec = seconds % 60
    if count_sec == 0:
        count_sec = "00"

    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if seconds > 0:
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

        timer = window.after(1000, count_down, seconds - 1)
        
    else:
        canvas.itemconfig(timer_text, text=f"0:00")
        start_count_down()




def reset():
    global timer
    global reps
    reps = 0
    check_marks.config(text="")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="OO:OO")













# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Pomodoro app")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tkinter.Canvas(width=300, height=300, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(150, 150, image=tomato_img)
timer_text = canvas.create_text(150,
                                150,
                                text="OO:OO",
                                fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=3, column=1)

mode = tkinter.Label(text="00:00",
                     font=("Arial", 30, "bold"),
                     fg=GREEN,
                     bg=YELLOW)
mode.grid(column=1, row=0)

start_button = tkinter.Button(text="Start", command=start_count_down)
start_button.grid(column=2, row=4)

reset_button = tkinter.Button(text="Reset", command=reset)
reset_button.grid(column=0, row=4)

check_marks = tkinter.Label(text="", bg=YELLOW, fg=GREEN)
check_marks.grid(row=5, column=1)

window.mainloop()
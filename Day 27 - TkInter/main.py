import tkinter


def miles_to_kilometer():
    value = float(input.get())
    km = value * 1.689
    my_label3.config(text=f"{km}")
    




window = tkinter.Tk()
window.title("TK inter")
window.minsize(width=500, height=400)
window.config(padx=10, pady=10)
#Entry
#Label
my_label = tkinter.Label(text="I Am fasf", font=("Arial", 10, "bold"))
my_label.config(text="is equal to")
my_label.grid(column=0, row=1)
my_label.config(padx=10, pady=10)

my_label1 = tkinter.Label(text="I Am a Label", font=("Arial", 10, "bold"))
my_label1.config(text="Km")
my_label1.grid(column=2, row=1)
my_label1.config(padx=10, pady=10)

my_label2 = tkinter.Label(text="I Am a Label", font=("Arial", 10, "bold"))
my_label2.config(text="miles")
my_label2.grid(column=2, row=0)
my_label2.config(padx=10, pady=10)


my_label3 = tkinter.Label(text="I Am a Label", font=("Arial", 10, "bold"))
my_label3.config(text="0")
my_label3.grid(column=1, row=1)
my_label3.config(padx=10, pady=10)


input = tkinter.Entry(width=10)
print(input.get())
input.grid(column=1, row=0)

#Button
button = tkinter.Button(text="Calculate", command=miles_to_kilometer)
button.grid(column=1, row=2)
button.config(padx=0, pady=0)



window.mainloop()

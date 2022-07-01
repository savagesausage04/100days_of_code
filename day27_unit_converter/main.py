from tkinter import *

window =Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)
window.config(padx=50, pady=20)


entry = Entry(width=10)
entry.grid(row=0, column=1)

miles = Label(text="Miles", font=("Courier", 24, "normal"))
miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to", font=("Courier", 24, "normal"))
is_equal_to.grid(row=1, column=0)

km = Label(text="km", font=("Courier", 24, "normal"))
km.grid(row=1, column=2)

num_km = Label(text="0")
num_km.grid(row=1, column=1)

def calculate_action():
    km_num = round(int(entry.get()) * 1.609)
    num_km.config(text=km_num)

calculate = Button(text="Calculate", command=calculate_action)
calculate.grid(row=2, column=1)


window.mainloop()

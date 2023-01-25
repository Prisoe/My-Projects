from tkinter import *

# Window
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=150, height=75)
window.config(padx= 20, pady=20)


# textbox/input
miles = Entry(width=5)
miles.grid(column=2, row=1)

# label
label = Label(text="Miles")
label.grid(column=3, row=1)

another_label = Label(text="is equal to:")
another_label.grid(column=0, row=3)

final_label = Label(text="Km")
final_label.grid(column=3, row=3)

answer_label = Label()
answer_label.grid(column=2, row=3)


# # textarea
# text = Text(height=1, width=5)
# text.grid()


# button
def calculate():
    value = int(miles.get())
    # print(type(value))
    kilometres = round(value * 1.60934)
    print(type(kilometres))
    answer_label.config(text=str(kilometres))


button = Button(text="Calculate", command=calculate)
button.grid(column=2, row=4)


window.mainloop()

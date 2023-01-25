from tkinter import *


def button_clicked():
    print("I got clicked")
    text = input_text.get()
    # my_label.config(text=text)

def action():
    print("New button got clicked")


# CREATE window object
window = Tk()
window.title("My First GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(column=0, row=0)
my_label.config(padx=15, pady=15)


# Button
button = Button(text="Click me", command=button_clicked)
# button.place(x=150, y=75)
button.grid(column=3, row=1)

button = Button(text="New button", command=action)
button.grid(column=6, row=0)


# Entry/ Input
input_text = Entry(width=20)
# returns input as a string
text_input = input_text.get()
print(text_input)
# input_text.pack(side="left")
input_text.grid(column=15, row=21)






# Keeps window open
window.mainloop()
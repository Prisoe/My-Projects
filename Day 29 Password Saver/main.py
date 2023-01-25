from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project


def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # List comprehensions
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    password = "".join(password_list)
    # for char in password_list:
    #     password += char

    password_text.insert(0, password)
    pyperclip.copy(password)


def search_file():
    key = website_text.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File found")
    else:
        if key in data:
            value = data[key]
            email = value["email"]
            password = value["password"]
            messagebox.showinfo(title=key, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showerror(title="Error", message=f"No saved details for {key}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():

    website = website_text.get().title()
    email = email_text.get()
    password = password_text.get()
    new_data = {website: {
        "Email": email,
        "Password": password,
    }}

    # Messagebox

    if len(website) == 0:
        messagebox.showerror(title="Website Error", message="Please enter website")

    elif len(password) == 0:
        messagebox.showerror(title="Password Error", message="Please enter password")
    # else:
    #     is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email: {email} "
    #                                                           f"\n Password: {password} \n Save? ")
    else:
        # print(website, email, password)
        try:
            with open("data.json", "r") as data_file:
                # read the data
                data = json.load(data_file)
                # # updating old data with new data
                # data.update(new_data)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                # Update data in json file
                json.dump(new_data, data_file, indent=4)

        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            # Load or read data from a Json file
            # data = json.load(data_file)
            # print(data)
            # Write to Data_json
            # json.dump(new_data, data_file, indent=4)

        finally:
            website_text.delete(0, "end")
            password_text.delete(0, "end")

    # ---------------------------- UI SETUP ------------------------------- #


# window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


# Canvas
canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0)


# Labels
website = Label(text="Website: ", font=("Cambria", 10))
website.grid(column=0, row=1)

email = Label(text="Email/Username: ", font=("Cambria", 10))
email.grid(column=0, row=2)

password = Label(text="Password: ", font=("Cambria", 10))
password.grid(column=0, row=3)


# Text area
website_text = Entry(width=25)
website_text.focus()
website_text.grid(column=1, row=1)

email_text = Entry(width=44)
email_text.insert(END, string="prosperalabi7@gmail.com")
email_text.grid(column=1, row=2, columnspan=2)

password_text = Entry(width=25)
password_text.grid(column=1, row=3)


# buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", command=add_password, width=36)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=search_file)
search_button.config(padx=30)
search_button.grid(column=2, row=1)

window.mainloop()

from tkinter import *
from tkinter import messagebox
from random import  shuffle, randint, choice
from pyperclip import copy
import json


# --------------------------------- GENERATE PASSWORD ------------------------------------------#

def generate_password():

    pass_input.delete(0, END)

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = randint(8, 10)
    nr_symbols = randint(2, 4)
    nr_numbers = randint(2, 4)

    password_letter = [choice(letters) for _ in range(nr_letters)]
    password_symbols = [choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letter + password_symbols + password_numbers

    shuffle(password_list)

    password = ""
    for char in password_list:
        password = "".join(password_list)

    pass_input.insert(0, password)
    copy(password)

# --------------------------------- SAVE PASSWORD ------------------------------------------#

def save():

    website = website_input.get()
    email = email_input.get()
    password = pass_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
                messagebox.showinfo(title="Success", message="Your password is saved")
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
                messagebox.showinfo(title="Success", message="Your password is saved")
        finally:
            website_input.delete(0,END)
            pass_input.delete(0,END)




# --------------------------------- GET PASSWORD ------------------------------------------#

def load_password():
    website = website_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            copy(password)
            messagebox.showinfo(title=f"We have found your password for {website}!",message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists.")






window = Tk()
window.title("Password Manager")
window.resizable(False,False)
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=2,row=1)


website_label = Label(text="Website:")
website_label.grid(column=1,row=2)
email_label = Label(text="email/Username:")
email_label.grid(column=1,row=3)
pass_label = Label(text="Password:")
pass_label.grid(column=1,row=4)


website_input = Entry(width=21)
website_input.grid(column=2,row=2)

email_input = Entry(width=35)
email_input.grid(column=2,row=3,columnspan=2)
email_input.insert(0,"mikolajbogacki13@gmail.com")

pass_input = Entry(width=21)
pass_input.grid(column=2,row=4)

load_pass_button = Button(text="Search", width=13 , command=load_password)
load_pass_button.grid(column=3,row=2)

generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(column=3,row=4)

add_pass_button = Button(text="Add",width=36, command=save)
add_pass_button.grid(column=2,row=5,columnspan=2)

window.mainloop()
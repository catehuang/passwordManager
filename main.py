from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = "Courier"
FILE = "data.txt"

window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=50, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)


def save_to_file():
    website = input_website.get()
    email = input_email.get()
    password = input_password.get()

    if not website or not email or not password:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title="Do you want to save it?", message=f"The details entered:" 
                         f"\nWebsite: {website}\nEmail: {email}\nPassword: {password}")

        if is_ok:
            with open(FILE, "a") as file:
                file.write(f"{website} | {email} | {password}\n")
            input_website.delete(0, END)
            input_password.delete(0, END)


def generate_password():
    gen_password = []
    password = ""
    letters = list(map(chr, range(97, 123)))
    numbers = list(i for i in range(10))
    symbols = ['!', '#', '$', '%', '&', '*', '+']

    pwd_lower_letters = [random.choice(letters) for _ in range(random.randint(3, 5))]
    pwd_upper_letters = [random.choice(letters).upper() for _ in range(random.randint(3, 5))]
    pwd_numbers = [str(random.choice(numbers)) for _ in range(random.randint(2, 4))]
    pwd_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    gen_password = pwd_lower_letters + pwd_upper_letters + pwd_numbers + pwd_symbols
    random.shuffle(gen_password)
    password = "".join(gen_password)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password) # copy it to clipboard


label_website = Label(text="Website", bg="white")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username", bg="white")
label_email.grid(row=2, column=0)

label_password = Label(text="Password", bg="white")
label_password.grid(row=3, column=0)

input_website = Entry(width=40, highlightthickness=2)
input_website.grid(row=1, column=1, columnspan=2, pady=10)
input_website.focus()

input_email = Entry(width=40, highlightthickness=2)
input_email.grid(row=2, column=1, columnspan=2, pady=10)
input_email.insert(0, "example@example.com")

input_password = Entry(width=30, highlightthickness=2)
input_password.grid(row=3, column=1, pady=10)

button_generate_password = Button(text="Generate", width=7, bg="white", command=generate_password)
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=49, bg="white",command=save_to_file)
button_add.grid(row=4, column=0, columnspan=3, pady=20)


window.mainloop()
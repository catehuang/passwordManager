from tkinter import *

FONT = "Courier"

window = Tk()
window.title("Password Manager")
window.config(pady=40, padx=50, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website", bg="white")
label_website.grid(row=1, column=0)

label_email = Label(text="Email/Username", bg="white")
label_email.grid(row=2, column=0)

label_password = Label(text="Password", bg="white")
label_password.grid(row=3, column=0)

input_website = Entry(width=40, highlightthickness=2)
input_website.grid(row=1, column=1, columnspan=2, pady=10)

input_email = Entry(width=40, highlightthickness=2)
input_email.grid(row=2, column=1, columnspan=2, pady=10)

input_password = Entry(width=30, highlightthickness=2)
input_password.grid(row=3, column=1, pady=10)

button_generate_password = Button(text="Generate", width=7, bg="white")
button_generate_password.grid(row=3, column=2)

button_add = Button(text="Add", width=49, bg="white")
button_add.grid(row=4, column=0, columnspan=3, pady=20)


window.mainloop()
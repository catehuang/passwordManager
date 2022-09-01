from tkinter import *

window = Tk()
window.title("Password Manager")
window.config(pady=20, padx=20, bg="white")
logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.pack()



window.mainloop()
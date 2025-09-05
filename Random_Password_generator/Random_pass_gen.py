import random
import string
import tkinter as tki
from tkinter import messagebox
from PIL import Image, ImageTk


def pass_gen():
    try:
        length = int(length_entry.get()) 

        
        if length < 4:
            messagebox.showerror("Error", "Password length should be >4!")
            return
        if length > 100:
            messagebox.showerror("Error", "Password length is too Long!")
            return

       
        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digits_var.get()
        use_special = special_var.get()

        
        characters = ""
        if use_upper:
            characters += string.ascii_uppercase
        if use_lower:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Error", "Select at least one chkbox!")
            return

        
        password = ''.join(random.choice(characters) for _ in range(length))
        result_var.set(password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid Length in numbers!")


def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard!")



root = tki.Tk()
root.title("Random Password Generator")
root.geometry("900x500")


bg_img = Image.open("dodge.jpg")
bg_img = bg_img.resize((900, 500))
bg = ImageTk.PhotoImage(bg_img)

bg_label = tki.Label(root, image=bg)
bg_label.image = bg
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

tki.Label(root, text="Generate random passwords of your Choice of length.", font=("Gabriola", 16)).pack(pady=7)

tki.Label(root, text="Password Length:", font=("Algerian", 14)).pack(pady=5)
length_entry = tki.Entry(root, width=5)
length_entry.insert(0, "12")
length_entry.pack(pady=5)


upper_var = tki.BooleanVar(value=True)
lower_var = tki.BooleanVar(value=True)
digits_var = tki.BooleanVar(value=True)
special_var = tki.BooleanVar(value=True)

tki.Checkbutton(root, text="Uppercase", variable=upper_var, font=("Gabriola", 12)).pack(pady=3)
tki.Checkbutton(root, text="Lowercase", variable=lower_var, font=("Gabriola", 12)).pack(pady=3)
tki.Checkbutton(root, text="Digits", variable=digits_var, font=("Gabriola", 12)).pack(pady=3)
tki.Checkbutton(root, text="Special Characters", variable=special_var, font=("Gabriola", 12)).pack(pady=3)


tki.Button(root, text="Generate Password", command=pass_gen, font=("Algerian", 14)).pack(pady=10)

result_var = tki.StringVar()
tki.Entry(root, textvariable=result_var, width=30).pack(pady=5)

tki.Button(root, text="Copy", command=copy_password, font=("Algerian", 12)).pack(pady=5)

root.mainloop()

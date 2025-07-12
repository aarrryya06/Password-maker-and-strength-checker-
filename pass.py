import random
import string
import tkinter as tk
from tkinter import messagebox

# ----- Strength Checker -----
def check_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score = sum([has_upper, has_lower, has_digit, has_symbol])

    if length < 6:
        return "Very Weak"
    elif score == 4 and length >= 12:
        return "Strong"
    elif score >= 3:
        return "Medium"
    else:
        return "Weak"

# ----- Password Generator -----
def generate_password():
    length = int(length_entry.get())
    chars = string.ascii_lowercase
    if use_upper.get():
        chars += string.ascii_uppercase
    if use_digits.get():
        chars += string.digits
    if use_symbols.get():
        chars += string.punctuation

    if length < 4:
        messagebox.showwarning("Too Short", "Password should be at least 4 characters.")
        return

    password = ''.join(random.choice(chars) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

    strength = check_strength(password)
    strength_label.config(text=f"Strength: {strength}")

# ----- GUI -----
root = tk.Tk()
root.title("Password Generator & Strength Checker")
root.geometry("400x300")
root.resizable(False, False)

# Length
tk.Label(root, text="Password Length:").pack()
length_entry = tk.Entry(root)
length_entry.insert(0, "12")
length_entry.pack()

# Options
use_upper = tk.BooleanVar()
use_digits = tk.BooleanVar()
use_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase", variable=use_upper).pack()
tk.Checkbutton(root, text="Include Numbers", variable=use_digits).pack()
tk.Checkbutton(root, text="Include Symbols", variable=use_symbols).pack()

# Password output
tk.Label(root, text="Generated Password:").pack()
password_entry = tk.Entry(root, width=30)
password_entry.pack()

# Strength Label
strength_label = tk.Label(root, text="Strength: ")
strength_label.pack()

# Buttons
tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

# Run
root.mainloop()

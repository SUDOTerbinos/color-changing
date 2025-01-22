import tkinter as tk
import random

def change_color():
    random_color = f"#{random.randint(0, 0xFFFFFF):06x}"
    root.config(bg=random_color)

root = tk.Tk()
root.title("Color Changer")
root.geometry("400x300")

button = tk.Button(root, text="Change Color", command=change_color, font=("Arial", 14))
button.pack(expand=True)

root.mainloop()

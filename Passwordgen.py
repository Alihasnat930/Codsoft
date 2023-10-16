import random
import string
import ttkbootstrap as ttk
from PIL import Image,ImageTk
from ttkbootstrap.constants import *

root = ttk.Window()
root.title("Password Generator")
frame = ttk.Frame(root, style="")
frame.pack(padx=10, pady=10, fill=ttk.BOTH, expand=True)
label = ttk.Label(frame, text="Password length", font=("Helvetica", 12))
label.pack()
password_length_entry = ttk.Entry(frame, style="info", font=("Helvetica", 12))
password_length_entry.pack()
def generate_password():
    password_length = password_length_entry.get()
    if not password_length:
        result_label.config(text="Error: Please enter a password length.")
        return
    try:
        password_length = int(password_length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(password_length))
        result_label.config(text="Generated password: " + password)
    except ValueError:
        result_label.config(text="Error: Password length must be a valid number.")
generate_button = ttk.Button(frame, text="Generate", command=generate_password,bootstyle="outline", style="success-outline")
generate_button.pack()
result_label = ttk.Label(frame, text="", style="success.TLabel",font=("Helvetica", 12))
result_label.pack()
image = Image.open("C:/Users/Ali/Downloads/password_icon.png")
photo = ImageTk.PhotoImage(image)
root.iconphoto(False, photo)
root.mainloop()

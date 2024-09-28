import tkinter
import json  # For saving and loading defaults
from generator import GenPass
from user_interactive import UserInteractive

# ---------------------------- UI SETUP ------------------------------- #
# Create a window
window = tkinter.Tk()
window.title("Password Manager V.1.1")
window.config(padx=15, pady=20)

# Create an image
canvas = tkinter.Canvas(width=200, height=200)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Create a title and inputbox
web_title = tkinter.Label(text="Website:", font=("Times New Roman", 14, "normal"))
web_title.grid(column=0, row=1, padx=10, sticky="w")
web_input = tkinter.Entry(width=24)
web_input.grid(column=1, row=1, columnspan=2, sticky="w", pady=10)
web_input.focus()

email_title = tkinter.Label(text="Email/Username:", font=("Times New Roman", 14, "normal"))
email_title.grid(column=0, row=2, padx=10)
email_input = tkinter.Entry(width=24)
email_input.grid(column=1, row=2, columnspan=2, sticky="w", pady=10)

pass_title = tkinter.Label(text="Password:", font=("Times New Roman", 14, "normal"))
pass_title.grid(column=0, row=3, padx=10, sticky="w")
pass_input = tkinter.Entry(width=24)
pass_input.grid(column=1, row=3, sticky="w", pady=10)

# Create an instance of GenPass
gen_pass = GenPass(pass_input)
gen_button = tkinter.Button(text="Generate Password", fg="white", background="#435334", command=gen_pass.generate_password)
gen_button.grid(column=2, row=3)

# Create an instance of UserInteractive
user_interactive = UserInteractive(web_input, email_input, pass_input)

# Buttons
search_button = tkinter.Button(text="Search", background="#CEDEBD", width=15, command=user_interactive.search_pass)
search_button.grid(column=2, row=1)

set_default_button = tkinter.Button(text="Set Default", bg="#9EB384", width=15, command=user_interactive.save_defaults)
set_default_button.grid(column=2, row=2)

user_interactive.load_defaults()        # Load default values after creating the UI components

clear_button = tkinter.Button(text="Clear_inputs", width=10, background="#FFB2B2", command=user_interactive.clear_inputs)
clear_button.grid(column=1, row=4, pady=10, sticky="w")

clear_button = tkinter.Button(text="Clear_data", width=10, background="#FFB2B2", command=user_interactive.clear_user_data)
clear_button.grid(column=1, row=4, pady=10, sticky="e", padx=10)

save_button = tkinter.Button(text="Save", width=15, background="green", fg="white", command=user_interactive.save_file)
save_button.grid(column=2, row=4, pady=10)

window.mainloop()
import tkinter as tk
from tkinter import filedialog
import webbrowser
from morse import ConvertToMorse

#_____________________________________________ Event function _______________________________________________________

# Function to clear pre-text when input box is clicked
def clear_pretext(event):
    current_text = input_box.get("1.0", "end-1c")
    if current_text.strip() == input_pretext:
        input_box.delete("1.0", "end")
        input_box.unbind("<Key>")  # Unbind the key event after pre-text is cleared

# Function to restore pre-text when input box loses focus and is empty
def restore_pretext(event):
    if not input_box.get("1.0", "end-1c").strip():
        input_box.insert("1.0", input_pretext)
        input_box.tag_add("pretext", "1.0", "end")
        input_box.tag_config("pretext", foreground="gray")

# Function to convert text to Morse code and live update output box
def get_output(event=None):
    input_text = input_box.get("1.0", "end-1c")
    morse_obj = ConvertToMorse(input_text)
    output_box.config(state="normal")  # Enable output box
    output_box.delete("1.0", "end")
    output_box.insert("1.0", morse_obj.converter())
    output_box.config(state="disabled")  # Disable output box again

# Create a Convert button to convert
# def get_output():
#     input_text = input_box.get("1.0", "end-1c")
#     morse_code = ConvertToMorse.convert_to_morse(input_text)
#     output_box.config(state="normal")  # Enable output box
#     output_box.delete("1.0", "end")
#     output_box.insert("1.0", morse_code)
#     output_box.config(state="disabled")  # Disable output box again

# Function to clear the input box
def clear_input_and_output():
    input_box.delete("1.0", "end")
    output_box.config(state="normal")  # Enable output box
    output_box.delete("1.0", "end")
    output_box.config(state="disabled")  # Disable output box again
    
# Function to save output to a file
def save_output():
    output_text = output_box.get("1.0", "end-1c")
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", 
                                             filetypes=[("Text files", "*.txt"), 
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(output_text)
            
# Function to open the URL in a web browser
def open_url(url):
    webbrowser.open(url)

# Function to handle URL click
def on_url_click(event):
    open_url(event.widget.url)
    
# Function to create a labeled URL
def create_url_label(parent, text, url):
    label = tk.Label(parent, text=text, font=("Times New Roman", 12, "underline"), fg="white", cursor="hand2", bg="#2C4E80")
    label.url = url  # Store the URL as an attribute of the label
    label.bind("<Button-1>", on_url_click)
    return label
    

#_____________________________________________ UI setup ___________________________________________________________

# Create the Tkinter window
window = tk.Tk()
window.title("Morse Code Converter")
window.config(padx=20,pady=30)
window['bg'] = "#2C4E80"

# Create a frame
my_frame = tk.Frame(window)
my_frame.grid(row=0, column=0)
my_frame['bg'] = "#2C4E80"

# Create an image
canvas = tk.Canvas(my_frame, width=300, height=200)
logo_img = tk.PhotoImage(file="img/Morse code receiver.png")
canvas.create_image(150, 100, image=logo_img)
canvas.grid(row=0)

# Input label
input_label = tk.Label(my_frame, text="Input:", font=("Times New Roman",14,"normal"), fg="#FFC55A", bg="#2C4E80")
input_label.grid(row=1, column=0, pady=(0,10), sticky="w")

# Input box
input_box = tk.Text(my_frame, width=100, height=10, font=("Consolas",13,"normal"))
input_box.grid(row=2, column=0, )

# Add pre-text to input box
input_pretext = "Type your text or morse code here..."
input_box.insert("1.0", input_pretext)
input_box.tag_add("pretext", "1.0", "end")
input_box.tag_config("pretext", foreground="gray")

# Scrollbar for the input box
input_scrollbar = tk.Scrollbar(my_frame, orient="vertical", command=input_box.yview)
input_scrollbar.grid(row=2, column=1, sticky="ns")
input_box.config(yscrollcommand=input_scrollbar.set)

# Bind click event to input box
input_box.bind("<Button-1>", clear_pretext)

# Bind focus-out event to input box
input_box.bind("<FocusOut>", restore_pretext)

# Bind key event to input box to remove pre-text
input_box.bind("<Key>", clear_pretext)

# Bind key release event to input box for live conversion
input_box.bind("<KeyRelease>", get_output)

# Clear button
clear_button = tk.Button(my_frame, text="Clear", command=clear_input_and_output, bg="#FFCF96")
clear_button.grid(row=1, column=0, pady=(0,10), sticky="e")

# Output label
output_label = tk.Label(my_frame, text="Output:", font=("Times New Roman",14,"normal"), fg="#CDFADB", bg="#2C4E80")
output_label.grid(row=3, column=0, pady=(20,10), sticky="w")

# Output box
output_box = tk.Text(my_frame, width=100, height=10, state="disabled", font=("Consolas",13,"normal"))
output_box.grid(row=4, column=0,)

# Scrollbar for the output box
output_scrollbar = tk.Scrollbar(my_frame, orient="vertical", command=output_box.yview)
output_scrollbar.grid(row=4, column=1, sticky="ns")
output_box.config(yscrollcommand=output_scrollbar.set)

# # Create a Convert button
# convert_button = tk.Button(window, text="Convert", command=get_output)
# convert_button.grid(row=5, column=0, pady=(30,10))

# Save button
save_button = tk.Button(my_frame, text="Save As", command=save_output, bg="#CDFADB")
save_button.grid(row=3, column=0, pady=(20,10), sticky="e")

# Label linking to a URL
morse_info = create_url_label(my_frame,"Click here for more information about morse code", "https://en.wikipedia.org/wiki/Morse_code")
morse_info.grid(row=5, column=0, padx=50, pady=(20, 10))

# Run the Tkinter event loop
window.mainloop()

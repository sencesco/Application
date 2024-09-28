import tkinter
from tkinter import messagebox
import json

DEFAULTS_FILE = 'defaults.json'

class UserInteractive:
    # ---------------------------- INSTANTIATE SETUP ------------------------------- #
    def __init__(self, web_input, email_input, pass_input):
        self.web = web_input
        self.email_usr = email_input
        self.pa = pass_input

    # ---------------------------- SAVE DEFAULT VALUES ------------------------------- #
    def save_defaults(self):
        defaults = {
            'email': self.email_usr.get(),
            'website': self.web.get()
        }
        with open(DEFAULTS_FILE, 'w') as file:
            json.dump(defaults, file)

    # ---------------------------- LOAD DEFAULT VALUES ------------------------------- #
    def load_defaults(self):
        try:
            with open(DEFAULTS_FILE, 'r') as file:
                defaults = json.load(file)
                self.email_usr.insert(0, defaults.get('email', ''))  # Populate email input
                self.web.insert(0, defaults.get('website', ''))  # Populate website input
        except FileNotFoundError:
            # If the file does not exist, do nothing (defaults will be empty)
            pass
        
    # ---------------------------- SAVE FILE INFO ------------------------------- #
    def save_file(self):
        self.new_data = {
            self.web.get(): {
                "email/username": self.email_usr.get(),
                "password": self.pa.get()
            }
        }
        
        if len(self.web.get()) == 0 or len(self.email_usr.get()) == 0 or len(self.pa.get()) == 0:
            messagebox.showwarning(title="Oops,", message="Please don't leave any fields empty!")
            return  # Early exit

        try:
            with open("data.json", "r") as file:
                # Reading old data
                self.data = json.load(file)
        except FileNotFoundError:
            # Create a new file if it does not exist
            with open("data.json", "w") as file:
                json.dump(self.new_data, file, indent=4)
            messagebox.showinfo(title="Saved", message="New entry has been saved.")
            return  # Early exit

        if self.web.get() in self.data:
            # If the website exists, get the existing password
            existing_password = self.data[self.web.get()]["password"]
            new_password = self.pa.get()
            # Ask user to confirm replacing the old password with the new one
            self.is_ok = messagebox.askokcancel(
                title="Do you want to proceed?",
                message=f"Website '{self.web.get()}' already exists.\n\n"
                        f"Existing Password: {existing_password}\n"
                        f"New Password: {new_password}\n\n"
                        f"Do you want to overwrite the existing password?"
            )
            if self.is_ok:
                self.data.update(self.new_data)
                with open("data.json", "w") as file:
                    json.dump(self.data, file, indent=4)
                messagebox.showinfo(title="Updated", message="Password has been updated.")
        else:
            # If the website is not in the data, add it
            self.data.update(self.new_data)
            with open("data.json", "w") as file:
                json.dump(self.data, file, indent=4)
            messagebox.showinfo(title="Saved", message="New entry has been saved.")

    # ---------------------------- FIND PASSWORD ------------------------------- # 
    def search_pass(self):
        self.website = self.web.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
            return  # Early exit

        if self.website in data:
            email = data[self.website]["email/username"]
            password = data[self.website]["password"]
            # Copy password to clipboard
            self.web.clipboard_clear()  
            self.web.clipboard_append(password)
            messagebox.showinfo(title=self.website, message=f"Email: {email}\nPassword: {password}\n\n(Password copied to clipboard.\nYou can paste it in somewhere.)")
        elif self.website == "":
            messagebox.showinfo(title="Error", message="Please provide a website name.")
        else:
            messagebox.showinfo(title="Error", message=f"No Email/Username for {self.website} exists.")
            
    # ---------------------------- CLEAR INPUTS ------------------------------- #
    def clear_inputs(self):
        self.web.delete(0, tkinter.END)         # Clear website input
        self.email_usr.delete(0, tkinter.END)   # Clear email input
        self.pa.delete(0, tkinter.END)          # Clear password input
        
    # ---------------------------- CLEAR USER DATA ------------------------------- #
    def clear_user_data(self):
        website_to_delete = self.web.get()  # Get the website input
        if len(website_to_delete) == 0:
            messagebox.showwarning(title="Oops,", message="Please provide a website name to delete.")
            return
        
        try:
            with open("data.json", "r") as file:
                self.data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
            return

        if website_to_delete in self.data:
            # Ask for confirmation before deletion
            confirm = messagebox.askokcancel(
                title="Confirm Deletion",
                message=f"Are you sure you want to delete the data for '{website_to_delete}'?"
            )
            if confirm:
                del self.data[website_to_delete]  # Delete the website entry
                with open("data.json", "w") as file:
                    json.dump(self.data, file, indent=4)  # Save updated data
                self.clear_inputs()
                messagebox.showinfo(title="Deleted", message=f"Data for '{website_to_delete}' has been deleted.")
            else:
                messagebox.showinfo(title="Cancelled", message="Deletion cancelled.")
        else:
            messagebox.showinfo(title="Error", message=f"No data found for '{website_to_delete}'.")
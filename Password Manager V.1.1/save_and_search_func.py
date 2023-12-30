import tkinter
from tkinter import messagebox
import json

class Save_and_Search:
    def __init__(self,web_input,email_input,pass_input):
        self.web = web_input
        self.email_usr = email_input
        self.pa = pass_input


# ---------------------------- SAVE FILE INFO ------------------------------- #
    def save_file(self):
        self.new_data = {
            self.web.get(): {
                "email/username": self.email_usr.get(),
                "password": self.pa.get()
            }
        }
        
        if len(self.web.get()) == 0 or len(self.email_usr.get()) == 0 or len(self.pa.get()) == 0:
            messagebox.showwarning(title="Oops,", message= "Please don't leave any fields empty!")
        # If not empty
        # Confirm user to check again before save information
        else:
            self.is_ok = messagebox.askokcancel(title="Do you want to proceed!", 
                    message=f"Your information:\nWebsite: {self.web.get()}\nEmail/Username: {self.email_usr.get()}\nPassword: {self.pa.get()}") 
            # If it's ok the save an information
            if self.is_ok:
                # If a file exists, it will open a file.
                try:
                    with open("data.json", "r") as file:
                        #Reading old data
                        self.data = json.load(file)
                # Create a new file if a file not exists       
                except FileNotFoundError:
                    # Write file, if exisitng will rewrite if not create new file
                    with open("data.json", "w") as file:
                        json.dump(self.new_data, file, indent=4)
                #Updating old data with new data, If a file exists
                else:
                    self.data.update(self.new_data)   
                    with open("data.json", "w") as file:
                        json.dump(self.data, file, indent=4)                
                finally:
                    self.web.delete(0, tkinter.END)  
                    self.pa.delete(0, tkinter.END)
                    

# ---------------------------- FIND PASSWORD ------------------------------- # 
    def Search_Pass(self):
        self.website = self.web.get()
        try:
            with open("data.json") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if self.website in data:
                email = data[self.website]["email/username"]
                password = data[self.website]["password"]
                messagebox.showinfo(title=self.website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message=f"No details for {self.website} exists.")

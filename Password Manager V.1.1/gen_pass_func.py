import tkinter
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
class GenPass:
        def __init__(self,pass_input):
                self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
                        'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                        'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
                self.pass_input = pass_input
                
        def generate_password(self):
                # Clear the previous password from pass_input when press gen_button again
                self.pass_input.delete(0, tkinter.END)
                # Random pass number in character list
                # "_" Use for nothing to do in a list conprehenssion
                self.rand_pass_letters = [random.choice(self.letters) for _ in range(random.randint(6,8))]
                self.rand_pass_symbols = [random.choice(self.symbols) for _ in range(random.randint(2,4))]
                self.rand_pass_numbers = [random.choice(self.numbers) for _ in range(random.randint(2,4))]
                self.rand_pass_list = self.rand_pass_letters + self.rand_pass_symbols + self.rand_pass_numbers

                # Random position of pass
                random.shuffle(self.rand_pass_list)
                # Join the pass into 1 word
                self.password = "".join(self.rand_pass_list)
                
                # Show on the pass textbox
                self.pass_input.insert(0, self.password)
                
                # To auto copy in clipboad and ready to paste in somewhere
                pyperclip.copy(self.password)
        
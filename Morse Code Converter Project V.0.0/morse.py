morse_dict = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "0": "-----",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "'": ".----.",
    '"': ".-..-.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-....-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    "$": "...-..-",
    "@": ".--.-.",
    " ": "/"
}



# input_text = input("Input text to convert to Morse code: ")

class ConvertToMorse:
  
    def __init__(self, input_text):
        self.input_text = input_text.upper()
        
    def converter(self):
        if self.input_text[0] in (".","_"):
            return self.convert_to_character()
        else:
            return self.convert_to_morse()
        
    def convert_to_morse(self):
        morse_list = []
        for ch in self.input_text:
            # for character not in morse code
            if ch not in morse_dict.keys():
              return f"this {ch} does not correspond to any character in the conversion table."
            morse_list.append(morse_dict[ch])
        morse_code = ' '.join(morse_list)
        return morse_code
    
    def convert_to_character(self):
        characters = []
        morse_code_list = self.input_text.split(' ')
        for code in morse_code_list:
            character = self.get_key_from_value(code)
            if character:
                characters.append(character)
            else:
                return f"The Morse code '{code}' does not correspond to any character in the conversion table."
        return ''.join(characters)
      
    def get_key_from_value(self, value):
        for key, val in morse_dict.items():
            if val == value:
                return key
        return None  # Return None if the value is not found in the dictionary
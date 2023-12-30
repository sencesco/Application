from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    # We can specify a datatype if paranertery by paramert: datatype
    # Inthis case if we pass only quiz_brain we can do it but will not no a data type
    # need to pass args in to parameter
    # And this line "q_text = self.quiz.next_question()" when wite a code next_question() will not show and active funciton
    # But evenif specify or not the function still can run it.
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.q_ans = ""    
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20, bg=THEME_COLOR)
        self.show_score = Label(text=f"Score: 0", font=("Arial",16,"italic"), bg=THEME_COLOR, fg="white")
        self.show_score.grid(column=1, row=0, sticky="e")
        
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=290, # for keep text with and if text over a with a remainig of text will go to a new line
            text= "",
            fill=THEME_COLOR, 
            font=("Arial", 16, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        # false_img and true_img not define will seft because need to use only inside this class, deosn't need outside can call
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.check_answer_true)
        self.false_button.grid(column=0, row=2)
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.check_answer_false)
        self.true_button.grid(column=1, row=2)
        replay_img = PhotoImage(file="images/restart.png")
        self.replay_button = Button(image=replay_img, foreground=THEME_COLOR, highlightthickness=0,command=self.replay)            

        
        self.get_next_questions() 
        
        self.window.mainloop()
            
    def get_next_questions(self):
        self.canvas.config(bg="white")
        if not self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text = f"Your final score was: {self.quiz.score}/{self.quiz.question_number}")
            self.false_button.grid_remove() # Hide a button
            self.true_button.grid_remove()
            self.replay_button.grid(column=0, row=2, columnspan=2)
            
        else:
            self.show_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        
    def check_answer_true(self):
        true_is_right = self.q_ans_true = self.quiz.check_answer("True")
        self.give_feedback(true_is_right)
        
    def check_answer_false(self):
        false_is_right = self.q_ans_true = self.quiz.check_answer("False")
        self.give_feedback(false_is_right)
        
    def give_feedback(self, is_rigth):
        if is_rigth == True:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_questions)
        
    def replay(self):
        self.canvas.itemconfig(self.question_text, text="")
        self.show_score.config(text="Score: 0")
        self.quiz.question_number = 0
        self.quiz.score = 0
        self.replay_button.grid_remove()
        self.false_button.grid(column=0, row=2) # Call a button
        self.true_button.grid(column=1, row=2)
        self.get_next_questions()  

        
        
        

        

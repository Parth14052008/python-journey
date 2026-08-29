

import random
from quizgame_ques import question_bank




class GiveQuestion:
    def __init__(self):
        # Select 10 unique random questions
        self.questions = random.sample(list(question_bank.keys()), 10)
        self.index = 0

    def next_question(self):
        question = self.questions[self.index]
        self.index += 1

        self.user_ans = input(f"{question}: ").strip().capitalize()
        self.real_ans = question_bank[question]


class check_ans:
    def __init__(self, user_output, act_ans,):
        self.user_ans = user_output
        self.act = act_ans
    def tell(self):
        if self.user_ans == self.act:
            return "correct"
           
        else:
            return "incorrect"

class marks:
    def __init__(self,see):
        self.points = 0
        self.see = see 
    def give_to_user(self):
        if self.see == "correct":
            self.points+=1
            return self.points
        else:
            return 0
        
print("welcome to game quiz \n this game is test of your gk \n rules simple you have tell answere in True or False")

no_ques = 1
mark = 0 
ques = GiveQuestion()
while no_ques <= 10 :
 
    
    ques.next_question()
    no_ques+=1
    display = check_ans(user_output=ques.user_ans,act_ans=ques.real_ans)
    show = display.tell()
    print(show)
    points = marks(show)
    x = points.give_to_user()
    if x == 1:
        mark+=1
    else:
        pass 
    print(f"Your Marks is {mark}/10")






        



        


    
    


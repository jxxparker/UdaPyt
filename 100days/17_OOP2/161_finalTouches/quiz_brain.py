#todos
#create a clas called QuizBrain.
#initialise the question_number to 0
#initialise the question_list to an input

class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     return False
        return self.question_number < len(self.question_list) #same as above

    #create a method called next_question()
    #this needs to retrieve the item at the current question_number from the question_list.
    #use the input() fxn to show the user the Questin text and ask for the user's answer.

    def next_question(self):
        current_question = self.question_list[self.question_number]
        correct_answer = current_question.answer
        
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False) ")
        
        self.check_answer(user_answer, correct_answer) 

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Right")
        else:
            print(f"Wrong")
        print(f"  Correct Answer: {correct_answer}")
        print(f"  Current Score: {self.score}/{self.question_number}")

    
        

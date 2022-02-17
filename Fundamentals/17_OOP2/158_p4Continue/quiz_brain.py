#todos
#create a clas called QuizBrain.
#initialise the question_number to 0
#initialise the question_list to an input

class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list

    #create a method called next_question()
    #this needs to retrieve the item at the current question_number from the question_list.
    #use the input() fxn to show the user the Questin text and ask for the user's answer.

    def next_question(self):
        current_question = self.question_list[0]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False)")

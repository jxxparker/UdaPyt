from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

 #WRITE for a loop to iterate over the question_data.
 #Create a question object from each entry in question data.
 #append each Question object to the question_bank

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
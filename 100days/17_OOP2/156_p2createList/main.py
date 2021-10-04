from question_model import Question
from data import question_data

question_bank = []
#contain a question bank and answer
for question in question_data:
    question_text = question["text"] #this will initialize the text from questioon_data in data.py
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)

    
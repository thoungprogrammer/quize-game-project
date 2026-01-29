from question_model import Question
from data import question_data 
from quiz_brain import QuizBrain
question_bank = [] # create an empty list to store question and answer

for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text = question_text ,q_answer = question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question(): # while False : Do nothing / While True : Do something
    quiz.next_question()
    
# You've completed the quiz.
# Your final score was: 10/12.
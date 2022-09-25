
from extras import question_data



class Question:

        def __init__(self, text, answer):
            self.text = text
            self.answer = answer




question_bank = []
q_run = 0

for something in question_data:
    question_bank.append(Question(text= question_data[q_run]['text'],answer= question_data[q_run]['answer']))
    q_run += 1






class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.questions_list = q_list
        self.score = 0
    
    def still_has_questions(self):
        return self.question_number < len(self.questions_list)
            

    def next_question(self):
        current_question = self.questions_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)? ").capitalize()
        self.check_answer(user_ans, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print(f'Thats wrong!\nThe correct ans is {correct_answer}')
        print(f'Your current score is {self.score}/{self.question_number}')    
        



quiz = QuizBrain(q_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"\nYou've completed the quiz.\nYour finals score is {quiz.score}/{quiz.question_number}")





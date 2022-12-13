
from data import question_data
from question_model import Question
from quiz_brain import QuizzBrain


text = ""
answer = ""
question_bank = []
for a in question_data:
    for b in a:
        if b == "text":
            text = a[b]
        else:
            answer = a[b]

    question = Question(text, answer)
    question_bank.append(question)
Game = QuizzBrain(question_bank)
while Game.still_has_questions():
    Game.next_question()


print(f"You completed the Quizz your score is {Game.score}/{Game.question_number}")


#You can get more quizz data from openquizz dB google it.
class QuizzBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        self.answer = input(f'{self.question_number}. {question.text} "True or False?')
        self.check_answer(self.answer, question.answer)

    def still_has_questions(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            return False

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print("you got it right!")
            self.score += 1
        else:
            print("you got it wrong!")

        print(f"The right answer is {correct_answer}")
        print(f"You score is {self.score}/{self.question_number}")
        print("\n")
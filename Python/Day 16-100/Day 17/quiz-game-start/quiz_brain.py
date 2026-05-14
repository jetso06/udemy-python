class QuizBrain:

    def __init__(self, questions_list):
        self.questions_list = questions_list
        self.questions_number = 0
        self.score=0

    def still_has_questions(self):
        return self.questions_number < len(self.questions_list)


    def next_question(self):
        current_question = self.questions_list[self.questions_number]
        self.questions_number += 1
        self.user_answer = input(f"Q.{self.questions_number}: {current_question.text}. (True/False): ").lower()
        self.check_answer(self.user_answer, current_question.answer)

    def check_answer(self, user_answer, answer):
        if self.user_answer == answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print(f"You got it wrong!")
        print(f"The correct answer was: {answer}.")
        print(f"Score: {self.score}/{self.questions_number}")
        print("\n")


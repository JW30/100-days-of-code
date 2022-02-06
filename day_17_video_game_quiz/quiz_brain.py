class QuizBrain:

    def __init__(self, questions):
        self.questions = questions
        self.question_number = 0
        self.score = 0

    def next_question(self):
        question = self.questions[self.question_number]
        self.question_number += 1
        answer = input(f"Q.{self.question_number}: {question.text} (True/False): ")
        self.check_answer(question.answer, answer)

    def has_next_question(self):
        if self.question_number < len(self.questions):
            return True
        print("You've completed the quiz!")
        print(f"Your final score was: {self.score}/{self.question_number}")
        return False

    def check_answer(self, question_answer, user_answer):
        if question_answer.lower() == user_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong.")
        print(f"The correct answer was: {question_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")

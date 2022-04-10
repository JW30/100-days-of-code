from question_model import Question


class QuizBrain:

    def __init__(self, q_list: list):
        self.question_number: int = 0
        self.score: int = 0
        self.question_list: list = q_list
        self.current_question: Question = self.question_list[self.question_number]

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        self.current_question: Question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

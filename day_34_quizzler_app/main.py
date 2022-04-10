from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import html
from ui import TriviaUI

question_bank: list = []
for question in question_data:
    question_text: str = html.unescape(question["question"])
    question_answer: str = html.unescape(question["correct_answer"])
    new_question: Question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz: QuizBrain = QuizBrain(question_bank)
ui: TriviaUI = TriviaUI(quiz)

from data import question_bank
from quiz_brain import QuizBrain

quiz = QuizBrain(question_bank)

while quiz.has_next_question():
    quiz.next_question()

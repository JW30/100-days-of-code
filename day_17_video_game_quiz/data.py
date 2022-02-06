import urllib.request
import json
import html
from question_model import Question


def get_questions():
    with urllib.request.urlopen("https://opentdb.com/api.php?amount=10&category=15&type=boolean") as url:
        return json.loads(url.read().decode())["results"]


question_bank = [Question(html.unescape(d["question"]), d["correct_answer"]) for d in get_questions()]

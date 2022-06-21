import random

from flask import Flask
app = Flask(__name__)

random_number = random.randint(0, 9)


@app.route("/")
def main():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route("/<int:number>")
def show_number(number):
    if number > random_number:
        return '<h1 style="color: red">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/2i06qrSENrXoc/giphy.gif">'
    elif number < random_number:
        return '<h1 style="color: green">Too low, try again</h1>' \
               '<img src="https://media.giphy.com/media/d1E2IByItLUuONMc/giphy.gif">'
    else:
        return '<h1 style="color: blue">You found me!</h1>' \
               '<img src="https://media.giphy.com/media/l0Exk8EUzSLsrErEQ/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)

import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
new_dict = {row["letter"]: row["code"] for (_, row) in data.iterrows()}

print("**** Welcome to the NATO Phonetic Alphabet Translator")
while True:
    word = input("**** Enter a word: ")
    if word == "quit":
        break
    try:
        out = [new_dict[f"{letter}"] for letter in word.upper()]
        print(f"**** Your word is spelled: {out}")
    except KeyError:
        print("**** Sorry, only letters allowed.")


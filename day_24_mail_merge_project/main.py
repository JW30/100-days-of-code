with open("Input/Letters/starting_letter.txt", "r") as letter:
    starting_letter = letter.read()

with open("Input/Names/invited_names.txt", "r") as invited:
    names = (name.strip() for name in invited.readlines())

for name in names:
    letter = starting_letter.replace("[name]", name)
    with open(f"Output/ReadyToSend/letter_to_{name}", "w") as final_letter:
        final_letter.write(letter)

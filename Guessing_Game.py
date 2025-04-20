
secret_word = "Giraffe"
guess = ""
guess_count: int = 0
guess_limit = 3
out_of_guesses = False
Clues = ["Clue - Animal", "Clue - Tall", "Clue - Animal", "Clue - Banana"]

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        if guess_count == 1:
            print(Clues[0])
        if guess_count == 2:
            print(Clues[1])


    else:
        out_of_guesses = True

if out_of_guesses:
    print("YOU LOSE!")
else:
    print("YOU WIN!")

if guess == secret_word:
    secret_word = "Monkey"
    guess = ""
    guess_count: int = 0
    guess_limit = 3
    out_of_guesses = False

while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
        if guess_count == 1:
            print(Clues[2])
        if guess_count == 2:
            print(Clues[3])

    else:
        out_of_guesses = True

if out_of_guesses:
     print("YOU LOSE!")
else:
     print("YOU WIN!")

















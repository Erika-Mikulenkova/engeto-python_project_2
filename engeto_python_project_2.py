"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Erika Mikulenková
email: erika.mikulenkova@gmail.com
discord: Erika M.
"""
import random

separator = ("-" * 50)

# Pozdrav:
def greeting():
    print("Hi there!",
          separator,
          "I've generated a random 4 digit number for you.",
          "Let's play a bulls and cows game.",
          separator,
          "Enter a number:",
          separator,
          sep="\n")

# Vytvoření tajného čísla:
def create_secret_number():
    number = list(range(1, 10))
    random.shuffle(number)
    return ''.join(map(str, number[:4]))

# Hádaní tajného čísla:
def guess_evaluation(secret_number, guess_number):
    bulls = 0
    cows = 0

    for i in range(4):
        if guess_number[i] == secret_number[i]:
            bulls = bulls + 1
        elif guess_number[i] in secret_number:
            cows = cows + 1

    return bulls, cows

# Hra:
def game_bulls_and_cows():
    greeting()
    secret_number = create_secret_number()
    attempts_number = 0

    while True:
        attempts_number = attempts_number + 1
        guess = input(">>> ")
                
        if len(guess) != 4 or not guess.isdigit() or "0" in guess[0] \
        or len(set(guess)) < 4:
            print("Invalid input. Enter a 4-digit number that does not",
                  "start with a zero and must not contain duplicates.",
                  separator,
                  sep="\n")
            continue
        
        bulls, cows = guess_evaluation(secret_number, guess)
        print(f"{bulls} {'bull' if bulls == 1 else 'bulls'}, " 
              f"{cows} {'cow' if cows == 1 else 'cows'}")
        print(separator)
      
        if bulls == 4:
            print(f"Correct, you've guessed the right number in {attempts_number} "
                  f"{'guess' if attempts_number == 1 else 'guesses'}!")
                  
            if attempts_number < 4:
                print("That's amazing!")
            elif 4 < attempts_number < 7:
                print("That's average!")
            else:
                print("Not so good.")
            break

if __name__ == "__main__":
    game_bulls_and_cows()
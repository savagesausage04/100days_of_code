from random import randint

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100.")
mode = input("Choose a difficulty. Type 'easy' or 'hard': ")
the_number = randint(1, 100)


def easy_game():
    attempts = 10
    while attempts != 0:
        print(f"You have {attempts} left to guess the number.")
        guess = int(input("Make a guess: "))
        if the_number > guess:
            print("Too low.")
        elif the_number < guess:
            print("Too high.")
        elif the_number == guess:
            print(f"{guess} was the number. Good job!")
            return
        attempts -= 1
    print("You're out of guesses :( you lose!")


def hard_game():
    attempts = 5
    while attempts != 0:
        print(f"You have {attempts} left to guess the number.")
        guess = int(input("Make a guess: "))
        if the_number > guess:
            print("Too low.")
        elif the_number < guess:
            print("Too high.")
        elif the_number == guess:
            print(f"{guess} was the number. Good job!")
            return
        attempts -= 1
    print("You're out of guesses :( you lose!")


if mode == "easy":
    easy_game()
elif mode == "hard":
    hard_game()

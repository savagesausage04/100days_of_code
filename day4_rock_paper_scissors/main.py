import random
from art import rock, paper, scissors
opponent_move = int(input("What do you choose? type 0 for rock, 1 for paper, or 2 for scissors.\n"))


if (opponent_move) == 0:
    print(rock)
elif (opponent_move) == 1:
    print(paper)
elif (opponent_move) == 2:
    print(scissors)

print("Computer chose:")

computer_move = random.randint(0, 2)

if int(computer_move) == 0:
    print(rock)
elif int(computer_move) == 1:
    print(paper)
elif int(computer_move) == 2:
    print(scissors)

if opponent_move == 0 and computer_move == 0:
    print("It is a draw.")
elif opponent_move == 1 and computer_move == 1:
    print("It is a draw.")
elif opponent_move == 2 and computer_move == 2:
    print("It is a draw.")
elif opponent_move == 0 and computer_move == 1:
    print("You lose.")
elif opponent_move == 0 and computer_move == 2:
    print("You win.")
elif opponent_move == 1 and computer_move == 0:
    print("You win.")
elif opponent_move == 1 and computer_move == 2:
    print("You lose.")
elif opponent_move == 2 and computer_move == 0:
    print("You lose.")
elif opponent_move == 2 and computer_move == 1:
    print("You win.")
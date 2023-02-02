import random

rock = 'Rock'
scissors = 'Scissors'
paper = 'Paper'
computer_move = ""
player_move = input("Chose [r]ock, [s]cissors or [p]aper: ")

if player_move == "r":
    player_move = rock
elif player_move == "s":
    player_move = scissors
elif player_move == "p":
    player_move = paper
else:
    raise SystemExit("Invalid Input. Please try again...")
print(f"Your choice is {player_move}.")
computer_random_num = random.randint(1, 3)

if computer_random_num == 1:
    computer_move = rock
elif computer_random_num == 2:
    computer_move = scissors
else:
    computer_move = paper

print(f"The computer chose {computer_move}.")

if (player_move == rock and computer_move == scissors) or (player_move == paper and computer_move == rock) or (player_move == scissors and computer_move == paper):
    print("You win!")
elif player_move == computer_move:
    print("Draw!")
else:
    print("You lose!")

# lesson 08 - loops for rock paper scissors game
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playAgain = True

while playAgain:
    playerChoice = input(
        "\nEnter... \n1 for Rock\n2 for Paper\n3 for Scissors\n\n")

    player = int(playerChoice)

    if player < 1 or player > 3:
        sys.exit("Invalid choice. Try again.")

    computerChoice = random.choice("123")
    computer = int(computerChoice)
    # computerChoice = random.randint(1, 3)

    print("\nYou chose: " + str(RPS(player).name) +
          "\nPython chose: " + str(RPS(computer).name) + "\n")

    if player == 1 and computer == 3:
        print("Player wins! 🎉")
    elif player == 2 and computer == 1:
        print("Player wins! 🎉")
    elif player == 3 and computer == 2:
        print("Player wins! 🎉")
    elif player == computer:
        print("It's a tie! 😲")
    else:
        print("Python wins! 🐍")

    playAgain = input("\nPlay again? (y/n): or \nQ to quit\n\n")
    if playAgain.lower() == "y":
        continue
    else:
        print('\n🎉🎉🎉🎉')
        print("Thank you for playing!\n")
        playAgain = False
        # break

sys.exit("Goodbye!")

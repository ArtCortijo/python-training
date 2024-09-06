# lesson05 - Rock Paper Scissors
import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


# print(RPS(2))
# print(RPS.ROCK)
# print(RPS['ROCK'])
# print(RPS.ROCK.value)

print("")
playerChoice = input("Enter... \n1 for Rock\n2 for Paper\n3 for Scissors\n\n")

player = int(playerChoice)

if player < 1 or player > 3:
    sys.exit("Invalid choice. Try again.")

computerChoice = random.choice("123")
computer = int(computerChoice)
# computerChoice = random.randint(1, 3)

print("")
print("You chose: " + str(RPS(player).name) +
      "\nPython chose: " + str(RPS(computer).name))
print("")

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

# Lesson 11 - rock paper scissors game
import sys
import random
from enum import Enum

game_count = 0


def play_rps():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input(
        "\nEnter... \n1 for Rock\n2 for Paper\n3 for Scissors\n\n")

    if playerChoice not in ['1', '2', '3']:
        print("Invalid choice. You must enter 1, 2 or 3.")
        return play_rps()

    player = int(playerChoice)

    computerChoice = random.choice("123")
    computer = int(computerChoice)
    # computerChoice = random.randint(1, 3)

    print("\nYou chose: " + str(RPS(player).name) +
          "\nPython chose: " + str(RPS(computer).name) + "\n")

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return "Player wins! 🎉"
        elif player == 2 and computer == 1:
            return "Player wins! 🎉"
        elif player == 3 and computer == 2:
            return "Player wins! 🎉"
        elif player == computer:
            return "It's a tie! 😲"
        else:
            return "Python wins! 🐍"

    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    game_count += 1

    print(f"\nGame count: {game_count}")

    print("\nPlay again?")

    while True:
        playAgain = input("\nY for Yes or \nQ to quit\n")
        if playAgain.lower() not in ['y', 'q']:
            print("Invalid choice. You must enter Y or Q.")
            continue
        else:
            break

    if playAgain.lower() == "y":
        return play_rps()
    else:
        print('\n🎉🎉🎉🎉')
        print("Thank you for playing!\n")
        sys.exit("Goodbye!")
        # break


play_rps()

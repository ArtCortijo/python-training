# Lesson 12 - rock paper scissors game
import sys
import random
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal player_wins
        nonlocal python_wins

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
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computer == 3:
                player_wins += 1
                return "Player wins! 🎉"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "Player wins! 🎉"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "Player wins! 🎉"
            elif player == computer:
                return "It's a tie! 😲"
            else:
                python_wins += 1
                return "Python wins! 🐍"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\nPlayer wins: {player_wins}")
        print(f"\nPython wins: {python_wins}")

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

    return play_rps


play = rps()
play()

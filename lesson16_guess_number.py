# Lesson 15 - Rock, Paper, Scissors
import sys
import random


def guess_number(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins

        playerChoice = input(
            f"\n{name}, guess which number I'm thinking of... \n1, 2 or 3\n\n")

        if playerChoice not in ['1', '2', '3']:
            print(f"{name}, please enter 1, 2 or 3.")
            return play_guess_number()

        computerChoice = random.choice("123")

        print(f"\n{name}, you chose: {playerChoice}")
        print(f"I was thinking about the number: {computerChoice}\n")

        player = int(playerChoice)
        computer = int(computerChoice)

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins

            if player == computer:
                player_wins += 1
                return f"{name} you win! 🎉"
            else:
                return f"Sorry, {name}. Better luck next time 🤷‍♂️"

        game_result = decide_winner(player, computer)
        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f'You winning percentaqe is: {player_wins/game_count:.2%}')
        print(f"\nPlay again, {name}?")

        while True:
            playAgain = input("\nY for Yes or \nQ to quit\n")
            if playAgain.lower() not in ['y', 'q']:
                print("Invalid choice. You must enter Y or Q.")
                continue
            else:
                break

        if playAgain.lower() == "y":
            return play_guess_number()
        else:
            print('\n🎉🎉🎉🎉')
            print("Thank you for playing!\n")
            if __name__ == "__main__":
                sys.exit(f"Goodbye {name}! 👋")

    return play_guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description='Provides a personalized game experience.')
    parser.add_argument('-n', '--name', metavar='name',
                        required=True, help='The name of the person playing the game.')
    args = parser.parse_args()

    guess_my_number = guess_number(args.name)
    guess_my_number()

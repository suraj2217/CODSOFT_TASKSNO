"""A command-line Rock, Paper, Scissors game with score tracking."""

import random


CHOICES = ("rock", "paper", "scissors")
BEATS = {"rock": "scissors", "scissors": "paper", "paper": "rock"}


def get_user_choice():
    """Prompt the user until they choose rock, paper, or scissors."""
    while True:
        choice = input("Choose rock, paper, or scissors: ").strip().lower()
        if choice in CHOICES:
            return choice
        print("Invalid choice. Please type rock, paper, or scissors.")


def decide_winner(user_choice, computer_choice):
    """Return the result of one round from the user's perspective."""
    if user_choice == computer_choice:
        return "tie"
    if BEATS[user_choice] == computer_choice:
        return "user"
    return "computer"


def main():
    user_score = 0
    computer_score = 0

    print("--- Rock, Paper, Scissors ---")
    print("Rock beats scissors, scissors beats paper, and paper beats rock.")

    while True:
        print("\nNew round")
        user_choice = get_user_choice()
        computer_choice = random.choice(CHOICES)
        winner = decide_winner(user_choice, computer_choice)

        print(f"You chose: {user_choice.title()}")
        print(f"Computer chose: {computer_choice.title()}")

        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            user_score += 1
            print("You win this round!")
        else:
            computer_score += 1
            print("Computer wins this round.")

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again not in ("yes", "y"):
            print("\nFinal score")
            print(f"You: {user_score} | Computer: {computer_score}")
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

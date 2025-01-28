import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    print("Welcome to Rock, Paper, Scissors!")
    print("Options: rock, paper, scissors")

    while True:
        # User input
        user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        # Computer choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        # Determine the winner
        if user_choice == computer_choice:
            print("It's a draw! Try again.")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            print("You win! 🎉")
            break
        else:
            print("Computer wins! 💻")
            break

# Run the game
rock_paper_scissors()

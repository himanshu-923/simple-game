import random


def stone_paper_scissors():
    print("\nStone Paper Scissors Game")
    user = input("Enter stone, paper or scissors: ").lower()
    options = ["stone", "paper", "scissors"]

    if user not in options:
        print("Invalid choice")
        return

    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("Match draw")
    elif user == "stone" and computer == "scissors":
        print("You win")
    elif user == "paper" and computer == "stone":
        print("You win")
    elif user == "scissors" and computer == "paper":
        print("You win")
    else:
        print("Computer wins")

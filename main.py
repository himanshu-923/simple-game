from stone_paper_scissors import stone_paper_scissors
from dice_roll import dice_roll


def game_menu():
    while True:
        print("\n----- GAME MENU -----")
        print("1. Stone Paper Scissors")
        print("2. Roll Dice")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            stone_paper_scissors()
        elif choice == "2":
            dice_roll()
        elif choice == "3":
            print("Thank you")
            break
        else:
            print("Invalid choice")


game_menu()

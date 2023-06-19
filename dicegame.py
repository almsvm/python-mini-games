import random

high_score = 0


def dice_game(high_score):
    min_val = 1
    max_val = 6

    while True:
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")

        choice = input("Enter your choice: ")

        if choice == "1" or choice.lower() == "Roll Dice":
            dice_1 = random.randint(min_val, max_val)
            dice_2 = random.randint(min_val, max_val)
            total = dice_1 + dice_2

            print('The values are:')
            print('Dice One: ', dice_1)
            print('Dice Two: ', dice_2)
            print('Total: ', total)
            print("Your score is: ", total)

        if total > high_score:
            high_score = total
            print("New high score: ", high_score)

        else:
            break


dice_game(high_score)

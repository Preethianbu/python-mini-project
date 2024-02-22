import random

min_val = 1
max_val = 6

roll_again = "yes"

while roll_again.lower() == "yes" or roll_again.lower() == "y":
    print("Rolling The Dices...")
    print("The Values are :")
    
    # Roll two dice
    dice1 = random.randint(min_val, max_val)
    dice2 = random.randint(min_val, max_val)
    
    # Print the values of the two dice
    print(dice1)
    print(dice2)
    
    # Determine the winner
    if dice1 > dice2:
        print("Player 1 wins!")
    elif dice1 < dice2:
        print("Player 2 wins!")
    else:
        print("It's a tie!")
    
    roll_again = input("Roll the Dices Again? (yes/no): ")

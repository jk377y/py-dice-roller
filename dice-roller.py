# import random module
import random

# defining the roll_dice() function
def roll_dice():
    # print the title of the program
    print("=== Dice Rolling Simulator ===")
    
    while True:
        # allows user to input the number of dice and the number of sides per dice
        num_dice = int(input("Enter the number of dice to roll: "))
        dice_sides = int(input("Enter the number of sides per dice: "))

        # this variable will store the result of each dice roll in an array
        dice_rolls = []

        # roll the dice
        for _ in range(num_dice):
            # random.randint(a, b) returns a random integer that is between 1 and `dice_sides`
            roll = random.randint(1, dice_sides)
            # adds the result of each dice roll to the array
            dice_rolls.append(roll)
        
        # print a message "Dice Rolls:" that serves as a header for the result of each dice roll
        print("\nDice Rolls:")
        # enumerate() returns an iterable object that contains the index and value of each element in the array, in this case, `dice_rolls` and sets the start index to 1
        for index, roll in enumerate(dice_rolls, start=1):
            # print the result of each dice roll in the format: Dice {index}: {roll}
            print(f"Dice {index}: {roll}")
        
        # sum and display the total sum of all the dice rolls
        total_sum = sum(dice_rolls)
        print("Total Sum:", total_sum)
        
        # ask the user if they want to roll again, if so, the dice_rolls will be cleared and the loop will start again
        choice = input("\nRoll again? (y/n): ")
        if choice.lower() != 'y':
            print("Goodbye!")
            break

# call the function
roll_dice()
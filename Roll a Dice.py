import numpy as np
dice_sides = int(input("Enter the number of sides for the dice (6/12): "))
dice = range (1, dice_sides)

num_rolls = int(input("Enter the number of times you want to roll the dice: "))

result = np.random.choice(dice, sides = num_rolls, replace = True)
print(result)
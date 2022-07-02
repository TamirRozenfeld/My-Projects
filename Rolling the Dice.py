import random

print("You have 6 tries")
number_of_roll = 0
question = input('Would you like to roll the dice [y/n]?\n')


while question != 'n' and number_of_roll< 5:
    number_of_roll += 1
    if question == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(die1, die2)
        question = input('Would you like to roll the dice [y/n]?\n')
    else:
        print('Invalid response. Please type "y" or "n".')
        question = input('Would you like to roll the dice [y/n]?\n')

print('Good-bye!')
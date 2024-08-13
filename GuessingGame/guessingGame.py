import random

def guess_number():
    rand_number = random.randint(1,20)

    while True:
        guess = int(input("Guess a number between 1 to 20:"))
        if rand_number < guess:
            print("The guess is too high!")
        elif rand_number > guess:
            print("The guess is too low!")
        else:
            print("You got it!")
            break

guess_number()
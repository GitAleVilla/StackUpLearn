import random

def guess_number():
    rand_number = random.randint(1,20)
    list_of_guesses = []

    while True:
        guess = int(input("Guess a number between 1 to 20:"))
        list_of_guesses.append(guess)

        if rand_number < guess:
            print("The guess is too high!")
        elif rand_number > guess:
            print("The guess is too low!")
        else:
            print("You got it!")
            break

    print("You guessed the following numbers: ", list_of_guesses)


guess_number()
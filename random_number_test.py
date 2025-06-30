from random import randrange

'''
Generate a random number from a range of 0 to 10
To adjust the range edit the values within the parentheses ()
The first number controls the lower bounds and the second controls the higher bounds
'''
# initial message
print("Welcome to the random number generator...\n"
          "A random number will be generated between 0 and 100.\n"
          "Try to guess the number in 10 tries.\n")

# start of game loop
while True:
    random_number = randrange(0, 100)
    print(random_number)

# variables are initialized
    guess = 101     # number outside of range
    counter = 0
    your_name_here = "James Light"

# start of guessing loop
    while True:
        counter += 1    # counter increment

        guess = int(input(f"Enter guess number {counter}: "))

        # guess is checked against target number
        if guess == random_number:
            print('That\'s right!')
            print('That took', counter, 'guesses.')
            break
        elif guess < random_number:
            print("Too low... try again.")
        else:
            print("Too high... try again.")

        # check if guess limit is reached
        if counter == 10:
            print("Sorry, out of tries")
            break

# loop to validate input and repeat game
    while True:
        repeat = input("Would you like to try again? (y/n): ")
        if repeat.lower() == "y" or repeat.lower() == "n":
            break
        else:
            print("Invalid input. Try again.")
    if repeat.lower() == "n":   # statement to end the game
        break

print(f"Completed by, {your_name_here}")
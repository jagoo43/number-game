import random

playing = True
number = str(random.randint(10, 20))

print("I will generate a number from 10 to 20, and you have to guess the number one at a time.")
print("The game ends when you get the correct answer.")

while playing:
    guess = input("Guess a number: ")
    if number == guess:
        print("You guessed correctly!")
        print("The number was", number)
        playing = False
    else:
        print("Your guess is not right, try again.")
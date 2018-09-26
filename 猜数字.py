import random

number = random.randint(0, 100)
print("Guess a magic number between 0 and 100")

guess = -1
while guess != number:
    guess = eval(input("Enter yours guess:"))
    if guess == number:
        print("Yes , the number is ", number)
    elif guess > number:
        print("You guess is too high")
    else:
        print("You guess is too low")

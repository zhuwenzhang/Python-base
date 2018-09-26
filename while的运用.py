import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input("What is " + str(number1) + "-" + str(number2) + "?"))
while number1 - number2 != answer:
    answer = eval(input("Wrong answer. Try again. What is " + str(number1) + "-" + str(number2) + "?"))

print("You got it!")

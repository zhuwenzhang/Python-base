import random

number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

answer = eval(input("what is " + str(number1) + "+" + str(number2) + "?"))

print(number1, "+", number2, "=", answer, "is", number1 + number2 == answer)

import random

lottery = random.randint(0, 99)

guess = eval(input("Enter your lottery pick (two digits): "))

lotteryDigit1 = lottery // 10
lotteryDigit2 = lottery % 10

guessDigit1 = guess // 10
guessDigit2 = guess % 10

print("The lottery number is ", lottery)

if guess == lottery:
    print("You win 10000")
elif lotteryDigit1 == guessDigit2 and lotteryDigit2 == guessDigit1:
    print("You win 3000")
elif lotteryDigit1 == guessDigit2 or lotteryDigit1 == guessDigit1 \
        or lotteryDigit2 == guessDigit2 or lotteryDigit2 == guessDigit1:
    print("You win 1000")
else:
    print("Sorry,no match")

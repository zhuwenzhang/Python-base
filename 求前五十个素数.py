n1 = 50
n = 10
count = 0
number = 2
print("The first 50 prime numbers are")

while count < n1:
    isPrime = True
    divisor = 2
    while divisor <= number / 2:
        if number % divisor == 0:
            isPrime = False
            break
        divisor += 1
    if isPrime:
        count += 1

        print(format(number, "5d"), end='')
        if count % n == 0:
            print()
    number += 1

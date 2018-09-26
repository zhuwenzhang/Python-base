import random

n1 = 1000000
number = 0
for i in range(n1):
    x = random.random() * 2 - 1
    y = random.random() * 2 - 1
    if x * x + y * y <= 1:
        number += 1

pi = 4 * number / n1
print("π的近似值为：", pi)

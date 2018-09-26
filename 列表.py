n = 5
numbers = []
sum = 0

for i in range(n):
    value = eval(input("Enter a new number:"))
    numbers.append(value)
    sum += value

average = sum / n

count = 0
for i in range(n):
    if numbers[i] > average:
        count += 1

print("Average is ", average)
print("Number of elements above the average is", count)

print("                     九九乘法表    ")
print("    ", end=' ')
for j in range(1, 10):
    print(" ", j, end='  ')
print()
print("-------------------------------------------------")

for i in range(1, 10):
    print(i, "|", end=' ')
    for j in range(1, 10):
        print(format(i * j, "4d"), end=' ')
    print()

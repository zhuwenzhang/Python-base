n = []

roW = eval(input())
n1 = eval(input())

for i in range(roW):
    n.append([])
    for m in range(n1):
        value = eval(input())
        n[i].append(value)

print(n)

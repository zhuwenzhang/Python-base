n = [[1, 2, 3], [5, 4, 2], [5, 6, 2]]

for i in range(len(n)):
    for b in range(len(n[i])):
        print(n[i][b], end=' ')

    print()

# 第二种
for i in n:
    for b in i:
        print(b, end=' ')

    print()

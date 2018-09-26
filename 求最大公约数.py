n1 = eval(input("请输入第一个数："))
n2 = eval(input("请输入第二个数："))

gys = 1
k = 2
while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        gys = k
    k += 1

print(n1, "和", n2, "的最大公约数是:", gys)

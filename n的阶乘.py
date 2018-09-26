def main():
    n = eval(input("请输入一个数："))
    print(n, "的阶乘为：", factorial(n))


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


main()

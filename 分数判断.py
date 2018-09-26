def getgrade(num1):
    if num1 > 90.0:
        return 'A'
    elif num1 > 80.0:
        return 'B'
    elif num1 > 70.0:
        return 'C'
    elif num1 >= 60.0:
        return 'D'
    else:
        return 'F'


def main():
    a = eval(input("请输入一个分数:"))
    print("分数的等级是:", getgrade(a))


main()

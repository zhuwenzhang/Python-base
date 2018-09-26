def hwc(s):
    if len(s) <= 1:
        return True
    elif s[0] != s[len(s) - 1]:
        return False
    else:
        return hwc(s[1:len(s) - 1])


def main():
    a = input("请输入一个字符串：")
    if hwc(a):
        print("是")
    else:
        print("不是")


main()

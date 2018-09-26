def main():
    s = input("input a string:").strip()
    if iss(s):
        print("Yes")
    else:
        print("No")


def iss(s):
    low = 0

    high = len(s) - 1

    while low < high:
        if s[low] != s[high]:
            return False
        low += 1
        high -= 1

    return True


main()

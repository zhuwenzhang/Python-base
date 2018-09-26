def sum(i1, i2):
    result = 0
    for i in range(i1, i2 + 1):
        result += i

    return result


def main():
    print("sum from 1 to 10 is", sum(1, 10))
    print("sum from 11 to 20 is", sum(11, 20))
    print("sum from 21 to 20 is", sum(21, 30))


main()

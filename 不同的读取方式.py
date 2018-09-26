def main():
    infile = open("D:\\朱文章 文件\\朱文章 python\\第十三章习题\\zwz.txt", "r")
    print("(1)Using read():")
    print(infile.read())
    infile.close()

    infile = open("D:\\朱文章 文件\\朱文章 python\\第十三章习题\\zwz.txt", "r")
    print("\n(2)Using read(number):")
    s1 = infile.read(1)
    print(s1)
    s2 = infile.read(1)
    print(repr(s2))
    infile.close()

    infile = open("D:\\朱文章 文件\\朱文章 python\\第十三章习题\\zwz.txt", "r")
    print("\n(3)Using readline():")
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    print(repr(line1))
    print(repr(line2))
    print(repr(line3))
    infile.close()

    infile = open("D:\\朱文章 文件\\朱文章 python\\第十三章习题\\zwz.txt", "r")
    print("\n(4) Using readlines():")
    print(infile.readlines())
    infile.close()


main()

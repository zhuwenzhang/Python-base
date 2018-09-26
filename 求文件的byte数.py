import os


def main():
    path = input("Enter a directory or a file:").strip()

    try:
        print(getSize(path), "byte")

    except:
        print("Directory or file does not exist")


def getSize(path):
    size = 0

    if not os.path.isfile(path):
        lst = os.listdir(path)
        for subdirectory in lst:
            size += getSize(path + "\\" + subdirectory)
    else:
        size += os.path.getsize(path)

    return size


main()

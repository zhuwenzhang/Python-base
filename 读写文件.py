import os.path
import sys


def main():
    f1 = input("Enter a source file:").strip()
    f2 = input("Enter a target file:").strip()

    if os.path.isfile(f2):
        print(f2 + " already exists")
        sys.exit()

    infile = open(f1, "r")
    outfile = open(f2, "w")

    countLines = countChars = 0
    for line in infile:
        countLines += 1
        countChars += len(line)
        outfile.write(line)
    print(countLines, "lines and ", countChars, "chars copied")

    infile.close()
    outfile.close()


main()

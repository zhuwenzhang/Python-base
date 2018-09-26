def main():
    filename = input("Enter a filename:").strip()
    infile = open(filename, "r")

    wordCounts = {}
    for line in infile:
        processLine(line.lower(), wordCounts)

    pairs = list(wordCounts.items())

    items = [[x, y] for (y, x) in pairs]

    items.sort()

    for i in range(len(items) - 1, len(items) - 11, -1):
        print(items[i][1] + "\t" + str(items[i][0]))


def processLine(line, wordCounts):
    line = replacePunctuations(line)
    words = line.split()
    for word in words:
        if word in wordCounts:
            wordCounts[word] += 1
        else:
            wordCounts[word] = 1


def replacePunctuations(line):
    for ch in line:
        if ch in "sdfsafaf":
            line = line.replace(ch, " ")

    return line


main()

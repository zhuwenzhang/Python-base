def main():
    answers = [['A', 'D', 'C'], ['A', 'B', 'A'], ['B', 'B', 'C']]

    key = ['A', 'B', 'C']

    for i in range(len(answers)):
        count = 0
        for j in range(len(answers[i])):
            if answers[i][j] == key[j]:
                count += 1

        print("Student", i + 1, "'s correct count is ", count)


main()

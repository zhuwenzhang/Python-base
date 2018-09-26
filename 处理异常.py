def main():
    while True:
        try:
            filename = input("Enter a filename:").strip()
            infile = open(filename,"r")
            break
        except IOError:
            print("File "+filename+" does not exist.Try again")

    print("exist")
main()
import pickle


def main():
    outfile = open("pickle.dat", "wb")
    pickle.dump(45, outfile)
    pickle.dump(56.6, outfile)
    pickle.dump("Programmer is fun", outfile)
    outfile.close()

    infile = open("pickle.dat", "rb")
    print(pickle.load(infile))
    print(pickle.load(infile))
    print(pickle.load(infile))
    infile.close()


main()

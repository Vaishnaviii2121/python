def main():
    FileName = input("Enter file name : ")

    try:
        fobj = open(FileName, "r")

        data = fobj.read()
        words = data.split()

        print("Total number of words in", FileName, ":", len(words))

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file")

if __name__ == "__main__":
    main()

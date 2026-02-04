def main():
    FileName = input("Enter file name : ")
    Word = input("Enter word to search : ")

    try:
        fobj = open(FileName, "r")
        data = fobj.read()

        if Word in data:
            print("Word", Word, "is present in", FileName)
        else:
            print("Word", Word, "is not present in", FileName)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file")

if __name__ == "__main__":
    main()

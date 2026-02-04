def main():
    FileName = input("Enter file name : ")
    Str = input("Enter string : ")

    try:
        fobj = open(FileName, "r")
        data = fobj.read()

        count = data.count(Str)
        print("Frequency of", Str, "is:", count)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file")

if __name__ == "__main__":
    main()

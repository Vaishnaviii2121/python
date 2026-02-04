def main():
    FileName = input("Enter file name : ")

    try:
        fobj = open(FileName, "r")

        count = 0
        for line in fobj:
            count = count + 1

        print("Total number of lines in", FileName, ":", count)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file")

if __name__ == "__main__":
    main()

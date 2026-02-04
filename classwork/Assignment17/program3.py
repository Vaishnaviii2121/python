def main():
    FileName = input("Enter file name : ")

    try:
        fobj = open(FileName, "r")

        for line in fobj:
            print(line, end="")

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file")

if __name__ == "__main__":
    main()

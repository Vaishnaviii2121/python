import sys

def main():
    if len(sys.argv) != 3:
        print("Invalid number of arguments")
        return

    try:
        fobj1 = open(sys.argv[1], "r")
        fobj2 = open(sys.argv[2], "r")

        data1 = fobj1.read()
        data2 = fobj2.read()

        if data1 == data2:
            print("Success")
        else:
            print("Failure")

        fobj1.close()
        fobj2.close()

    except FileNotFoundError:
        print("Unable to open file")

if __name__ == "__main__":
    main()

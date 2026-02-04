def main():

    FileName = input("Enter File Name : ")

    try:
        fobj = open(FileName,"r")
        print("File opens Successfully\n")

        Data = fobj.read()
        print("Contents of file are :\n",Data)

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file")

if __name__=="__main__":
    main()

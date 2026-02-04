def main():
    Source = input("Enter source file name : ")
    Destination = input("Enter destination file name : ")

    try:
        fsrc = open(Source, "r")
        fdest = open(Destination, "w")

        data = fsrc.read()
        fdest.write(data)

        print("Contents of", Source, "copied into", Destination)

        fsrc.close()
        fdest.close()

    except FileNotFoundError:
        print("Unable to open source file")

if __name__ == "__main__":
    main()

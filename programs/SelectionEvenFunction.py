def ChechEven(no):
    if(no % 2 == 0):
        print("It is Even")
    else:
        print("It is Odd")

def main():
    ChechEven(11)               # positional argument
    ChechEven(no = 12)          # keyword Argument

if __name__ == "__main__":
    main()

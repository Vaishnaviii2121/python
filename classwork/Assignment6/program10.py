Max = lambda No1, No2, No3: No1 if (No1 >= No2 and No1 >= No3) else (No2 if No2 >= No3 else No3)

def main():
    value1 = int(input("Enter First Number: "))
    value2 = int(input("Enter Second Number: "))
    value3 = int(input("Enter Third Number: "))

    Ret = Max(value1, value2, value3)

    print("Maximum Number is", Ret)

if __name__ == "__main__":
    main()

def Maximum(Data):
    max = Data[0]

    for no in Data:
        if no > max:
            max = no

    return max

def main():
    size = 0
    value = 0

    print("Enter number of elements:")
    size = int(input())

    Data = list()

    print("Enter elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    Ret = Maximum(Data)
    print("Maximum number is:", Ret)

if __name__ == "__main__":
    main()

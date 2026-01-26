def Addititon(Data):
    sum = 0
    for no in Data:
        sum = sum + no
    return sum

def main():
    value = 0
    size = 0

    print("Enter Number of elements:")
    size = int(input())

    Data = list()

    print("Input Elements :")
    for i in range(size):
        value = int(input())
        Data.append(value)

    Ret = Addititon(Data)
    print("Addition is:",Ret)


if __name__ == "__main__":
    main()

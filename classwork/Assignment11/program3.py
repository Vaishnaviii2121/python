from functools import reduce

Greater = lambda No : No >=70 and No<=90

Increase = lambda No : No+10

Product = lambda No1,No2 : No1 * No2

def main():
    size = 0
    value = 0

    print("Enter the Number of elements :")
    size = int(input())

    Data = list()

    print("Enter elements:")
    for i in range(size):
        value = int(input())
        Data.append(value)

    FData = list(filter(Greater,Data))
    print("Data after Filter is :",FData)

    MData = list(map(Increase,FData))
    print("Data after map :",MData)

    RData = reduce(Product,MData)
    print("Data after reduce :",RData)


if __name__ == "__main__":
    main()

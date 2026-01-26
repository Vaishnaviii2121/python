from functools import reduce

Even = lambda No : No % 2 == 0

Square = lambda No : No * No 

Addition = lambda No1 ,No2 : No1 + No2

def main():
    value = 0
    size = 0

    print("Enter ther Number of Elements :")
    size = int(input())

    Data = list()

    print("Enter elements :")
    for i in range(size):
        value = int(input())
        Data.append(value)

    FData = list(filter(Even,Data))
    print("Data after filter :",FData)

    MData = list(map(Square,FData))
    print("Data after Map :",MData)

    RData = reduce(Addition,MData)
    print("Data after reduce :",RData)
        

if __name__ == "__main__":
    main()

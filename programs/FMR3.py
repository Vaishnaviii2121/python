from functools import reduce

def CheckEven(no):
    return (no % 2 ==0)

def Increament(no):
    return no + 1

def Add(A,B):
    return A + B

def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual Data is :",Data)

    FData = list(filter(CheckEven,Data))
    print("Data after Filter is :",FData)

    MData = list(map(Increament,FData))
    print("Data after map is :",MData)

    RData = reduce(Add,MData)
    print("Data after Reduce is :",RData)

if __name__ == "__main__":
    main()


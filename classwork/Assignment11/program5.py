from functools import reduce

def prime(No):
    if No <=1:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

def Multiply(No):
    return No * 2 

def Maximum(No1 ,No2):
    if No1 > No2:
        return No1
    else:
        return No2

def main():
    value = 0
    size = 0
    Ret = 0

    print("Enter ther Number of Elements :")
    size = int(input())

    Data = list()

    print("Enter elements :")
    for i in range(size):
        value = int(input())
        Data.append(value)

    FData = list(filter(prime,Data))
    print("Data after filter :",FData)

    MData = list(map(Multiply,FData))
    print("Data after Map :",MData)

    
    RData = reduce(Maximum,MData)
    print("Data after reduce :",RData)
    

if __name__ == "__main__":
    main()

from functools import reduce

CheckEven = lambda no : (no % 2 == 0)

Increament = lambda no : (no + 1)

Add = lambda A,B : (A + B)

def filterX(task,elements):
    Result = list()

    for no in elements:
        Ret = task(no)

        if(Ret == True):
            Result.append(no)

    return Result

def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual Data is :",Data)

    FData = list(filterX(CheckEven,Data))
    print("Data after Filter is :",FData)

    MData = list(map(Increament,FData))
    print("Data after map is :",MData)

    RData = reduce(Add,MData)
    print("Data after Reduce is :",RData)

if __name__ == "__main__":
    main()


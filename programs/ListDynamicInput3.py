def summition(Arr):
    sum = 0

    for i in range(len(Arr)):
        sum = sum + Arr[i]

    return sum
    

def main():
    size = 0
    value = 0
    Ret = 0

    print("Enter the Number of Element :")
    size = int(input())

    Data = list()
    
    print("Enter the elements :")
    for i in range(size):
        value = int (input())
        Data.append(value)

    Ret = summition(Data)

    print("Summition is : ",Ret)
    
if __name__ == "__main__":
    main()

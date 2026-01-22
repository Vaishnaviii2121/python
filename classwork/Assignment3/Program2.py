def CountDigit(No):
    count = 0

    if No == 0:
        return 1
    
    while No != 0:
        count = count + 1
        No = No // 10
        
    return count

def main():
    Ret = 0
    value = int(input("Enter Number :"))
    Ret = CountDigit(value)

    print("Count of Digits :",Ret)

if __name__=="__main__":
    main()

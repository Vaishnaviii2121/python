Min = lambda No1,No2 : No1 < No2
    
def main():
    value1 = int(input("Enter First Number:"))
    value2 = int(input("Enter Second Number:"))

    Ret = Min(value1,value2)

    if (Ret == True):
        print("Minimum Number is ",value1)
    else:
        print("Minimum Number is",value2)

if __name__=="__main__":
    main()

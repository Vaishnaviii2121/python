def ChkGreater(No1,No2):
    if(No1>No2):
        return True
    else:
        return False  

def main():
    Value1 = int(input("Enter first Element :"))
    value2 = int(input("Enter second Element :"))
    Ret = 0

    Ret = ChkGreater(Value1,value2)

    if(Ret == True):
        print(Value1,"is greater")
    else:
        print(value2,"is greater")

if __name__=="__main__":
    main()

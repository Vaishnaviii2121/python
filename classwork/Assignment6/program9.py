Multiply = lambda No1, No2 : (No1*No2)
    
def main():
    value1 = int(input("Enter First Number:"))
    value2 = int(input("Enter second Number:"))

    Ret = Multiply(value1,value2)

    print("Multiplication is :",Ret)

if __name__=="__main__":
    main()

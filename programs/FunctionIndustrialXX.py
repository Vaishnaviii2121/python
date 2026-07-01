def ChechEven(no):
    return (no % 2 == 0)       # Code Reduction

def main():
    Value = 0 
    Ret = False      

    print("Enter Number :")
    Value = int(input())

    Ret = ChechEven(Value)

    if(Ret == True):
        print("It is Even")
    else:
        print("It is Odd")
   
if __name__ == "__main__":
    main()


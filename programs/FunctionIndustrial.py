# procedural

def ChechEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False

def main():
    Value = 0 
    Ret = False      

    print("Enter Number :")
    Value = int(input())

    Ret = ChechEven(Value)

    print(Ret)

   
if __name__ == "__main__":
    main()


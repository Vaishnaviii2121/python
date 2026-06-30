# procedural

def ChechEven(no):
    if(no % 2 == 0):
        print("It is Even")
    else:
        print("It is Odd")

def main():
    Value = 0       # we can also write NONE, but we know value is integer hence 0 given 

    print("Enter Number :")
    Value = int(input())

    ChechEven(Value)

   
if __name__ == "__main__":
    main()


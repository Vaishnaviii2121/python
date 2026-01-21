def cube(No):
    Result = No * No * No

    return Result

def main():
    Ret = 0
    value = int(input("Enter Number :"))
    Ret = cube(value)

    print("Cube of Number is :",Ret)

if __name__ =="__main__":
    main()

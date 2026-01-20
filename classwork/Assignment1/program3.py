def square(No):

    Result = 0

    for _ in range(1,No):
        Result = No*No

    return Result

def main():
    value = int(input("Enter Number :"))
    Ret = 0

    Ret = square(value)

    print(Ret)

if __name__=="__main__":
    main()

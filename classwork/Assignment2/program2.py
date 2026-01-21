def Natural(No):
    for i in range(1,No,1):
        No = No + i
    return No

def main():
    num = int(input("Enter Number :"))
    Ret = Natural(num)

    print(Ret)

if __name__=="__main__":
    main()

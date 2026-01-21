def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i

    return Fact

def main():
    Ret = 0
    value = int(input("Enter Number :"))
    
    Ret = Factorial(value)

    print(Ret)

if __name__=="__main__":
    main()

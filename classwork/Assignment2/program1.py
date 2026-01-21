def Multiplication(No):

    for i in range(1,11): 
        print(No * i) 

def main():
    value = int(input("Enter Number :"))
    Ret = 0

    Ret = Multiplication(value)

if __name__=="__main__":
    main()

Even = lambda No : (No % 2 == 0)
    
def main():
    value = int(input("Enter Number:"))

    Ret = Even(value)

    if(Ret == True):
        print("Even")
    else:
        print("Odd")

if __name__=="__main__":
    main()

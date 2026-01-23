Odd = lambda No : (No % 2 != 0)
    
def main():
    value = int(input("Enter Number:"))

    Ret = Odd(value)

    if(Ret == True):
        print("Odd")
    else:
        print("Even")

if __name__=="__main__":
    main()

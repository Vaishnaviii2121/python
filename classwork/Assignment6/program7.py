Divisible_By_5 = lambda No : (No % 5 == 0)
    
def main():
    value = int(input("Enter Number:"))

    Ret = Divisible_By_5(value)

    if(Ret == True):
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")

if __name__=="__main__":
    main()

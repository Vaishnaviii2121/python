def Divisible(No):

    if(No % 3 == 0) and (No % 5 == 0):
        return True
    else:
        return False

def main():
    
    value = int(input("Enter Number :"))

    Ret = Divisible(value)

    if Ret == True:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")


if __name__=="__main__":
    main()

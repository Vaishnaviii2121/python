def prime(No):
    if No <= 1:
        return False
    
    for i in range(2,No):
        if No % i == 0:
            return False
        
    return True

def main():
    Ret = 0
    value = int(input())
    Ret = prime(value)

    if Ret == True:
        print("Prime Number")
    else:
        print("Not Prime Number")

if __name__=="__main__":
    main()

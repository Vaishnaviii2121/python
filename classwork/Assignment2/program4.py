def Even(No):
    
    for i in range(1,No+1):
        if ((i % 2)==0):
            print(i)

def main():
    value = int(input("Enter Number :"))
    Ret = 0

    Ret = Even(value)

if __name__ == "__main__":
    main()

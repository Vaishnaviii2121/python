def Display(No):
    
    if(No == 0):
        print("Zero")
    elif(No < 0):
        print("Negative Number")
    else:
        print("Positive Number")

def main():
    value = int(input("Enter Number :"))
    Display(value)

if __name__=="__main__":
    main()

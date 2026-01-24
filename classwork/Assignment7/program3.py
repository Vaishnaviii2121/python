Odd = lambda No : (No % 2 != 0)
    
def main():
    Data  =  [1,2,3,4,5,6,7]

    FData = list(filter(Odd,Data))
    print("Data after Filter is :",FData)

if __name__=="__main__":
    main()

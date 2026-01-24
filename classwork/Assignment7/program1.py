square = lambda no : (no * no)
    
def main():
    Data = [1,2,3,4,5]

    print("Actual Data is :",Data)

    MData = list(map(square,Data))
    print("Data after map is :",MData)

if __name__=="__main__":
    main()

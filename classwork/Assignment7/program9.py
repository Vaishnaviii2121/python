from functools import reduce
Product = lambda No1, No2 : No1 * No2 

def main():
    Data = [1,2,3,4,5,6,7]

    RData = reduce(Product,Data)
    print("Data after reduce :",RData)

if __name__ == "__main__":
    main()

Divisible = lambda No : (No % 3 == 0) and (No % 5 == 0)

def main():
    Data = [30,31,32,33,34,35,36]

    FData = list(filter(Divisible,Data))
    print("Data after filter :",FData)

if __name__ == "__main__":
    main()

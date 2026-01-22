def AreaOfRectangle(length,width):
    area = length * width

    return area

def main():
    value1 = int(input("Enter Length: "))
    value2 = int(input("Enter width: "))

    Ret = AreaOfRectangle(value1,value2)

    print("Area of rectangle :",Ret)

if __name__ == "__main__":
    main()

def AreaOfCircle(radius):
    pi = 3.14
    area = pi * radius * radius

    return area

def main():
    value = int(input("Enter Radius: "))

    Ret = AreaOfCircle(value)

    print("Area of circle :",Ret)

if __name__ == "__main__":
    main()

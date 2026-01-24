def ChkNum(number):
    if number % 2 == 0:
        return True
    else:
        return False

def main():
    num = int(input())

    Ret = ChkNum(num)

    if Ret == True:
        print("Even Number")
    else:
        print("Odd Number")

if __name__ == "__main__":
    main()

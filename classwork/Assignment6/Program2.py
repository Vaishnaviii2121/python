cube = lambda no : (no * no * no)
    
def main():
    value = int(input("Enter Number:"))
    Ret = cube(value)

    print("cube :",Ret)

if __name__=="__main__":
    main()

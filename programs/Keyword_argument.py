def EmployeeInfo(Name,Age,Salary,City):
    print("Name :",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)

def main():
    # Positional
    #EmployeeInfo("Rahul",26,2000.50,"Pune")         # Correct
    #EmployeeInfo(26,"Rahul","pune",2000.50)        # Wrong 

    # Keyword Argument
    EmployeeInfo(Age=26,Name="Rahul",City="pune",Salary=2000.50)            # Corrrect

if __name__ == "__main__":
    main()

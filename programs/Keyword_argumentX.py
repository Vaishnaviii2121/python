def EmployeeInfo(Name,Age,Salary,City):
    print("Name :",Name)
    print("Age :",Age)
    print("Salary :",Salary)
    print("City :",City)

def main():
    
    # Keyword Argument
    EmployeeInfo(Age=26,Name="Rahul",City="pune",Salary=None)            # Corrrect

if __name__ == "__main__":
    main()

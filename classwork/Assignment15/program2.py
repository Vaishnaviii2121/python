class BankAccount:
    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter name : ")
        self.Amount = int(input("Enter amount : "))

    def Display(self):
        print("Enter Account Holder Name : ",self.Name)
        print("Current Balance :",self.Amount)

    def Deposit(self):
        money = int(input("Enter amount to deposit :"))
        self.Amount = self.Amount + money
        print("Amount deposited successfully")

    def Withdraw(self):
        money = int(input("Enter amount to Withdraw :"))
        if money <= self.Amount:
            self.Amount = self.Amount - money
            print("Amount Withdrwn successfully")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest

    
obj1 = BankAccount()
obj2 = BankAccount()

obj1.Display()
obj1.Deposit()
obj1.Withdraw()
print("Interest :", obj1.CalculateInterest())

print("--------------------")

obj2.Display()
obj2.Deposit()
obj2.Withdraw()
print("Interest :", obj1.CalculateInterest())


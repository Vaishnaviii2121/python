no = 11             # Global variable   

def fun():        
    no = 21
    print("Value of no from fun is : ",no)      # 21
    no = no + 1    
    print("Value of no from fun is : ",no)      # 22

print("value of no is :",no)                    # 11
fun()
print("value of no is :",no)                    # 11


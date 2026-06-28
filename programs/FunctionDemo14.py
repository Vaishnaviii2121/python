def Phoenix():
    print("Inside Phoenix Mall")

    def Zara():
        print("Inside ZARA")
        
    Zara()      # if zara() call is at indentation level 2 then it will cause Recursion

def main():
   Phoenix()
    
if __name__ =="__main__":
    main()

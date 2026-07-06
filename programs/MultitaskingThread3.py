import threading

def Display():
    print("Inside Display Function :",threading.get_ident())
    for i in range(100):
        print("Inside Display")

def main():
    print("Inside Main :",threading.get_ident())

    T = threading.Thread(target=Display)
    T.start()

    print("End of main")
    
if __name__ == "__main__":
    main()

    

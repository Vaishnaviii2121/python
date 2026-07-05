import threading

def Display():
    print("Inside Display Function :",threading.get_ident())

def main():
    print("Inside Main :",threading.get_ident())

    T = threading.Thread(target=Display)
    T.start()

    print("End of main")
    
if __name__ == "__main__":
    main()

    

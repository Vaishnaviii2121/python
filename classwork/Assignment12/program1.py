import threading

def Even(No):
    print("Even thread")
    for i in range(2,21,2):
        print(i)

def Odd(No):
    print("Odd thread")
    for i in range(1,20,2):
        print(i)

def main():
    
    t1 = threading.Thread(target=Even,args=(10,))
    t2 = threading.Thread(target=Odd,args=(10,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    
if __name__ == "__main__":
    main()

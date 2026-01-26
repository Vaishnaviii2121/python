import threading

def isPrime(No):
    if No <= 1:
        return False
    for i in range(2, No):
        if No % i == 0:
            return False
    return True

def Prime(data):
    print("Prime numbers:")
    for no in data:
        if isPrime(no):
            print(no, end=" ")
    print()

def NonPrime(data):
    print("Non-prime numbers:")
    for no in data:
        if not isPrime(no):
            print(no, end=" ")
    print()

def main():
    Data = [10, 11, 12, 13, 14, 15, 17]

    t1 = threading.Thread(target=Prime, args=(Data,))
    t2 = threading.Thread(target=NonPrime, args=(Data,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
  

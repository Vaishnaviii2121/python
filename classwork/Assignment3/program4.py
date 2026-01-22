def palindrome(num):
    original = num
    rev = 0

    while num != 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num = num // 10

    if original == rev:
        return True
    else:
        return False


def main():
    value = int(input("Enter a number: "))

    if palindrome(value):
        print("Palindrome")
    else:
        print("NOT a Palindrome")


if __name__ == "__main__":
    main()

def reverse_number(num):
    rev = 0

    while num != 0:
        digit = num % 10
        rev = (rev * 10) + digit
        num = num // 10

    return rev


def main():
    value = int(input("Enter a number: "))
    result = reverse_number(value)
    print("Reverse number is:", result)


if __name__ == "__main__":
    main()

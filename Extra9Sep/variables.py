def main():
    number1 = " "
    number2 = " "
    while not number1.isdigit() or not number2.isdigit():
        number1 = input("Enter value 1: ")
        number2 = input("Enter value 2: ")


    # number1 och number2 är strängar med bara numeriska värden

    number1 = int(number1)
    number2 = int(number2)

    result = number1 / number2
    print(result)


if __name__ == '__main__':
    main()

def main():
    # En int kan vara oändligt stor och oändligt liten i Python
    # En int lagrar hela tal
    number = 10

    # En float representerar tal med decimaler
    number_float = 34.9

    name = "Joakim"

    print(name.upper())
    print(name)

    while True:
        number_as_string = input("Enter a number: ")
        if number_as_string.isdigit():
            number_as_string = int(number_as_string)
            break
        else:
            print("Please enter digits only!")
    print(number_as_string + 2)

    number_as_string = ""
    while not number_as_string.isdigit():
        number_as_string = input("Enter a number: ")
        if not number_as_string.isdigit():
            print("Please enter digits only!")

    print(int(number_as_string) + 2)


if __name__ == '__main__':
    main()

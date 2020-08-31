def main():
    persons = []

    while True:
        person = {}

        person["First"] = input("Enter the first name of a person: ")
        person["Last"] = input("Enter the last name of a person: ")
        persons.append(person)
        answer = input("Enter more persons? ")
        if answer.lower() == "n":
            break

    print(persons)


if __name__ == '__main__':
    main()

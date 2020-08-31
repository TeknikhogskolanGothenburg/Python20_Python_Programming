def main():
    person = {"First": "Anna", "Last": "Smith"}
    print(person["Last"])
    person["First"] = "Bob"
    person["Age"] = 22

    print(person)

if __name__ == '__main__':
    main()

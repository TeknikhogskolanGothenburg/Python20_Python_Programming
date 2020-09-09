def main():
    more = True
    while more:
        answer = input("More y/n? ")
        more = not answer.lower() == "n"
        #if answer.lower() == "n":
        #    more = False

    number = 10000

    while number > 100:
        number = number / 3
        #if number < 100:
        #    break
        print(number)

    print("Klar")

if __name__ == '__main__':
    main()

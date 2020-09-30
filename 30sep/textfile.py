def main():
    file = open("textfile.txt", "w")
    file.write("Hej hej\n")
    file.write("Bye\n")
    file.close()

    with open("textfile.txt", "a") as file:
        file.write("Hepp\n")
        file.write("Hopp\n")


if __name__ == '__main__':
    main()

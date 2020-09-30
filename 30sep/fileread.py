def main():
    with open("textfile.txt", "r") as file:
        text = file.readlines()


    with open("textfile.txt", "r") as file:
        line = file.readline()
        print(line.strip())
        line = file.readline()
        print(line.strip())

    print("-------------")
    for line in open("textfile.txt", "r"):
        print(line.strip())


if __name__ == '__main__':
    main()

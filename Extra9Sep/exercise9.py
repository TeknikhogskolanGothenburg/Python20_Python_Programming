def main():
    word = "hello"
    vowels = "aeiouy"
    for letter in word:
        if letter in vowels:
            print(letter.upper(), end="")
        else:
            print(letter, end="")


if __name__ == '__main__':
    main()

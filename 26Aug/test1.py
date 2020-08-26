def main():
    name = "Doris"
    hidden_word = "__r__"
    new_name = ""
    for i, character in enumerate(name):
        if character == "i":
            new_name = new_name + "i"
        else:
            new_name = new_name + hidden_word[i]
    print(new_name)


if __name__ == '__main__':
    main()

def main():
    name = input("Enter your name: ")
    if name.lower() == 'eva':
        print("Vilket superfint namn du har Eva")
    else:
        if name[1] == 'v':
            print("Yes du är bäst")
        else:
            if name[1] == 'u':
                print("Bingo")
            else:
                print("Jaha, någon skall ju heta det")


    if name.lower() == 'eva':
        print("Vilket superfint namn du har Eva")
    elif name[1] == 'v':
        print("Yes du är bäst")
    elif name[1] == 'u':
        print("Bingo")
    else:
        print("Jaha, någon skall ju het det")

if __name__ == '__main__':
    main()

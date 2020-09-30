def tja(func):
    def tjoho():
        func()
        print("tjoho")
    return tjoho

@tja
def hej():
    print("hej")

@tja
def hopp():
    print("hopp")


def main():
    hej()
    hopp()
    hej()


if __name__ == '__main__':
    main()

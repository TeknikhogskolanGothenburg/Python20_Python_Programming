# LEGB
value = 10

def function():
    value = 11
    print(value)

    def inner():
        value = 12
        print(value)

    inner()


def main():
    print(value)
    function()


if __name__ == '__main__':
    main()

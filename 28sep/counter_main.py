import my_math


def add(a, b):
    return a + b + 10


def main():
    result = my_math.add(3, 4)
    print(result)
    result = add(3, 4)
    print(result)
    result = my_math.sub(3, 4)
    print(result)
    result = my_math.mul(3, 4)
    print(result)
    result = my_math.div(3, 4)
    print(result)


if __name__ == '__main__':
    main()

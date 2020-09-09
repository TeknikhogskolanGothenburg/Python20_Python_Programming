def func1(value):
    value += 1
    print(value)


def func2(sequence):
    sequence.append("Stefan")
    print(sequence)


def main():
    x = 10
    func1(x)
    print(x)

    names = ["Anna", "Pelle", "Lisa", "Ove"]
    func2(names.copy())
    print(names)


if __name__ == '__main__':
    main()

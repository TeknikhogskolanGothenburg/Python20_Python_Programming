def main():
    values = ([1, 2, 3], [4, 5, 6], [7, 8, 9])
    values[1].clear()
    print(values)
    first, second, third = values
    print(first)
    print(second)
    print(third)

    one_list = [1]
    one_tuple = (1, )
    print(type(one_list))
    print(type(one_tuple))


if __name__ == '__main__':
    main()

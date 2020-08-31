def main():
    numbers = [45, 2, 3, 14, 5, 78, 6]
    things = ["Hej", 1, True, 45.6]
    values = [1, 2, 3, 1, 2, 3, 1, 2, 3]

    things.append(99)
    things.insert(-1, "Tja")
    print(things)

    a_thing = things[2]
    print(a_thing)

    while 2 in values:
        values.remove(2)
    print(values)

    numbers2 = sorted(numbers, reverse=True)
    print(numbers)
    print(numbers2)
    numbers[3] = "Tre"
    print(numbers)

if __name__ == '__main__':
    main()

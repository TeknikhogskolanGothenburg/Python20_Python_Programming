def main():
    values = [3, 1, 6, 3, 9, 2, 4]
    while True:
        swapped = False
        for i in range(len(values)-1):
            if values[i] > values[i+1]:
                swapped = True
                values[i], values[i+1] = values[i+1], values[i]

        if not swapped:
            break
    print(values)



if __name__ == '__main__':
    main()

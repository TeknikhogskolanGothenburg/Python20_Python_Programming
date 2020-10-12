def get_input(split=False):
    value = input("Enter a value")
    if split:
        if " " in value:
            return value.split()
    if value == 'True' or value == 'False':
        return bool(value)
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value

def main():
    pass


if __name__ == '__main__':
    main()

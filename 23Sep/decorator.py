def modify(func):
    def inner(name):
        return "<<<" + func(name) + ">>>"
    return inner

@modify
def produce(name):
    return f"Hello {name}"

def main():
    result = produce("Bill")
    print(result)


if __name__ == '__main__':
    main()

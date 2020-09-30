def flatten(values, new_list=None):
    if new_list is None:
        new_list = []
    for thing in values:
        if isinstance(thing, list):
            flatten(thing, new_list)
        else:
           new_list.append(thing)
    return new_list


def main():
    values = [[[2, 3], 1], [4, 5], [6, 7, 8]]
    result = [item[0] for item in values]
    print(result)



if __name__ == '__main__':
    main()

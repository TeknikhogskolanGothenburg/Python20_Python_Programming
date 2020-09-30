import pickle

def main():

    persons = []
    with open("person.dat", "rb") as person_file:
        while True:
            try:
                person = pickle.load(person_file)
                persons.append(person)
            except EOFError:
                break

    for person in persons:
        print(person)



if __name__ == '__main__':
    main()

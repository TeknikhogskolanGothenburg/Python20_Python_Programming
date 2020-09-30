import pickle
from person import Person
import os

def main():
    p1 = Person("Stina", 43)
    p2 = Person("Kalle", 66)


    persons = [p1, p2]

    with open("person.dat", "ab") as person_file:
        for person in persons:
            pickle.dump(person, person_file)

    print(os.stat("person.dat"))

if __name__ == '__main__':
    main()

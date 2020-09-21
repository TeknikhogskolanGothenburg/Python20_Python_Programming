class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name}, {self.last_name}"

    def say_hi(self):
        print(f"Hello I am {self.first_name}!")


class User(Person):
    def __init__(self, first_name, last_name, user_name, password):
        super().__init__(first_name, last_name)
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return f"{super().__str__()} has the username {self.user_name} and has password {self.password}"


class Employee(Person):
    amount = 1.02

    def __init__(self, first_name, last_name, salary):
        super().__init__(first_name, last_name)
        self.salary = salary

    def __str__(self):
        return f"{super().__str__()} earns {self.salary}"

    def pay_rise(self):
        self.salary *= self.amount


class Developer(Employee):
    amount = 1.04

    def say_hi(self):
        print(f"Yo, I'm a developer and my name is {self.first_name}")


def main():
    e1 = Employee("Lisa", "Andersson", 38000)
    e2 = Employee("Pelle", "Nilsson", 32000)
    e3 = Employee("Stina", "Svensson", 45000)
    d1 = Developer("John", "Persson", 39000)
    u1 = User("Olle", "Karlsson", "olle", "s3cr37")

    people = [e1, e2, e3, d1, u1]
    for person in people:
        person.say_hi()





if __name__ == '__main__':
    main()

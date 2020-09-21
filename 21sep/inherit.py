class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def as_str(self):
        return f"a = {self.a} b = {self.b}"


class B(A):
    def __init__(self, a, b, c, d):
        super().__init__(a, b)
        self.c = c
        self.d = d

    def as_str(self):
        return f"{super().as_str()} c = {self.c} d = {self.d}"



def main():
    b_obj = B(1, 2, 3, 4)
    result = b_obj.as_str()

    print(result)



if __name__ == '__main__':
    main()

import pandas as pd
from matplotlib import pyplot
from dataclasses import make_dataclass

Person = make_dataclass("Person", [
    ('age', int),
    ('height', float),
    ('weight', float),
    ('chest', float),
    ('size', str),
    ('color', str)
], namespace={
    '__str__': lambda self: f'{self.age},{self.height},{self.weight},{self.chest},{self.size},{self.color}\n'
})


def prepare_data(df):
    ages = df.Age.tolist()
    heights = [s/10 for s in df.stature.tolist()]
    weights = [w/10 for w in df.weightkg.tolist()]
    chests = [c/10 for c in df.chestcircumference.tolist()]
    for i in range(len(ages)):
        age = ages[i]
        height = heights[i]
        weight = weights[i]
        chest = chests[i]
        if chest < 84:
            size = "XX-Small"
            color = "pink"
        elif 84 <= chest < 90:
            size = "X-Small"
            color = "yellow"
        elif 90 <= chest < 95:
            size = "Small"
            color = "red"
        elif 95 <= chest < 102:
            size = "Medium"
            color = "blue"
        elif 102 <= chest < 112:
            size = "Large"
            color = "lawngreen"
        elif 112 <= chest < 123:
            size = "X-Large"
            color = "green"
        elif 123 <= chest < 133:
            size = "XX-Large"
            color = "slategray"
        else:
            size = "XXX-Large"
            color = "black"
        person = Person(age, height, weight, chest, size, color)
        print(person)


def main():
    df = pd.read_csv('female.csv', index_col=0)
    prepare_data(df)


if __name__ == '__main__':
    main()

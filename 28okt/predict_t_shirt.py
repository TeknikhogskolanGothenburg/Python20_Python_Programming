from math import sqrt
import pandas as pd
from matplotlib import pyplot


def get_neighbors(k, weight, height, data_list):
    dists = []
    for point in data_list:
        x = point[1]
        y = point[0]
        size = point[3]
        dist = sqrt((weight-x)**2 + (height-y)**2)
        dists.append({'dist': dist, 'size': size})
    dists.sort(key=lambda d: d['dist'])
    return dists[:k]


def predict(neighbors):
    sizes = {}
    for dist in neighbors:
        size = dist['size']
        if size in sizes:
            sizes[size] += 1
        else:
            sizes[size] = 1
    total = len(neighbors)
    return {size: value / total * 100 for size, value in sizes.items()}



def main():
    data_female = pd.read_csv('cleaned_female.csv', index_col=0)
    data_male = pd.read_csv('cleaned_male.csv', index_col=0)

    number_of_rows = len(data_female) + len(data_male)

    weight, height = input("Enter your weight and height: ").split()
    weight = float(weight)
    height = float(height)
    marker_style = dict(color='lavender', marker="X", markersize=10)

    _, ax = pyplot.subplot()

    ax.scatter(data_female.Weight, data_female.Height, c=data_female.Color)
    ax.scatter(data_male.Weight, data_male.Height, c=data_male.Color)
    pyplot.plot(weight, height, fillstyle='none', **marker_style)
    pyplot.xlabel("Weight (kg)")
    pyplot.ylabel("Height (cm)")
    pyplot.show()

    data_list = data_male.values.tolist() + data_female.values.tolist()
    n = int(sqrt(number_of_rows))
    k_values = [3, 4, 5, 6, 7, 8, 9, 10, 11, n]

    for k in k_values:
        neighbors = get_neighbors(k, weight, height, data_list)
        result = predict(neighbors)
        print(f"I predict that you should get a t-shirt size of (k={k}):")
        for size, proc in result.items():
            print(f'\t{size} with a confidence of {proc:.2f}%')
        print("------------------------")


if __name__ == '__main__':
    main()

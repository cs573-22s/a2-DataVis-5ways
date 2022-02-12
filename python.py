import pandas as pd
import matplotlib.pyplot as plt
from scipy.sparse import data


def main():
    data = pd.read_csv("cars-sample.csv")
    weight = data["Weight"]
    mpg = data["MPG"]
    manufacturer = data['Manufacturer']
    colors = {"ford": "#90EE90",
              "bmw": "#f6938c",
              "honda": "#CCCC00",
              "mercedes": "#45bced",
              "toyota": "#EE82EE"}
    plt.scatter(
        weight,
        mpg,
        color=[colors[i] for i in manufacturer],
        alpha=0.5,
        s=weight / 20)
    plt.xlabel('Weight')
    plt.ylabel('MPG')
    plt.show()

if __name__ == "__main__":
    main()


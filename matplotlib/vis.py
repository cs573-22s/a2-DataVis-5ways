from __future__ import annotations # Weird type hinting
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

class DataPoint():
    # Data Point Struct to make categorization easier
    def __init__(self, manufacturer="NA", weight=0.0, mpg=0.0, bad = False):
        self.manufacturer = manufacturer
        self.weight = weight
        self.mpg = mpg
        self.bad = bad
    
    def __repr__(self):
        return "DataPoint(manufacturer = {man}, weight = {w}, mpg = {mpg}" \
            .format( 
                man = self.manufacturer,
                w = self.weight,
                mpg = self.mpg
            )

    @staticmethod 
    def instance_of(line : str) -> DataPoint:
        """
        Reads in a line of data and converts it to a DataPoint object
        """
        parts = [part.strip() for part in line.split(",")]
        if parts[2] == "NA" or parts[3] == "NA" or parts[7] == "NA":
            return DataPoint(bad = True)
        else:
            return DataPoint(manufacturer=parts[2], mpg=float(parts[3]), weight=float(parts[7]))

def main():
    # Import the data
    with open("../cars-sample.csv") as file:
        lines = file.readlines()[1:] # skip the first line
        data_points = [point for point in [DataPoint.instance_of(line) for line in lines] if not point.bad]

    groups = {}
    for point in data_points:
        if point.manufacturer not in groups:
            groups[point.manufacturer] = [point]
        else:
            groups[point.manufacturer].append(point)

    print(groups)
    

if __name__ == "__main__":
    main()
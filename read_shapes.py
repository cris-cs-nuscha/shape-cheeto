"""
read from shapes csv data file
"""

import csv

def read_csv(fname='shapes.csv'):
    """read shapes data from csv file and return list of dictionaries, or None"""
    with open(fname, encoding='utf-8') as f:
        shapes_list = []
        reader = csv.DictReader(f,skipinitialspace=True)
        for row in reader:
            # TODO, add to list intead of printing
            shapes_list += [row]
        return shapes_list 


# if running this script by itself, just print the list
if __name__ == '__main__':
    shapes = read_csv()
    print(shapes)
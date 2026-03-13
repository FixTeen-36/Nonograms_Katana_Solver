import csv
import os


def write_pattern(name: str, x_elements: list, y_elements: list) -> None:
    name += '.csv'
    if name in os.listdir('data'):
        print("The pattern with this name is already existing!")
        return
    with open(f'data\{name}', 'w', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)

        writer.writerow([len(x_elements)])
        for row in x_elements:
            writer.writerow(row)
        for row in y_elements:
            writer.writerow(row)


def read_pattern(name: str) -> list:
    try:
        with open(f'data\{name}.csv', newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            data = list(reader)

            m = int(data[0][0])
            x_elements = []
            y_elements = []
            for row in data[1:(m + 1)]:
                x_elements.append([int(x) for x in row])
            for row in data[(m + 1):]:
                y_elements.append([int(x) for x in row])

            if x_elements and y_elements:
                return x_elements, y_elements
            
    except FileNotFoundError:
        print(f"There is no pattern with name '{name}'!")
        print("Please, select a pattern from the list:")
        for i, name in enumerate(os.listdir('data'), 1):
            print(f"{i:2d}: {name[:-4]}")
        return [[1]], [[1]]

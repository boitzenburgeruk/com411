import csv


def export(path, export_number):
    print("Exporting...")
    with open(path, "a") as file:
        reader = csv.reader(file)

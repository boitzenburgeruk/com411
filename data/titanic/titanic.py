import csv

records = []
headings = []


def load_data(file_path):
    print("Loading data...")
    with open(file_path) as file:
        reader = csv.reader(file)
        heading = next(reader)
        headings.append(heading)
        for line in reader:
            records.append(line)
        file.close()
    print("Done!")


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records")


if __name__ == "__main__":
    run()
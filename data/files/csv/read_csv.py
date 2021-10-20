import csv


def read(path):
    print("Headings:")
    with open("bots.csv") as file:
        reader = csv.reader(file)
        headings = next(reader)
        print(headings)
        print("Values:")
        for line in reader:
            print(line)
    file.close()


def run():
    read("bots.csv")


if __name__ == "__main__":
    run()

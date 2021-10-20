import csv


def extract(path):
    print("Extracting...")
    with open(path) as file:
        reader = csv.reader(file)
        ignore = next(reader)
        names = ""
        for line in reader:
            names = names + line[1] + "\n"
        print("Done! The extracted names are: ")
        print(names)
        file.close()


def run():
    extract("bots.csv")


if __name__ == "__main__":
    run()
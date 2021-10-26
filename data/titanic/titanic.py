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


def display_menu():
    print("""
Please select of the following options:
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group""")
    choice = int(input())
    return choice


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")


if __name__ == "__main__":
    run()
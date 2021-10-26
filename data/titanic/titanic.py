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


def display_passenger_names():
    print("The names of the passengers are...")
    for record in records:
        passenger_name = record[3]
        print(passenger_name)


def display_num_survivors():
    num_survived = 0
    for record in records:
        survival_status = int(record[1])
        if survival_status == 1:
            num_survived += 1
    print(f"{num_survived} passengers survived")


def display_passengers_per_gender():
    females = 0
    males = 0
    for record in records:
        sex = record[4]
        if sex == "male":
            males += 1
        elif sex == "female":
            females += 1
    print(f"Females: {females}, Males: {males}")


def display_passengers_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    for record in records:
        # solution copied from SOL
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
            elif age < 65:
                adults += 1
            else:
                elderly += 1
    print(f"Children: {children}, Adults: {adults}, Elderly: {elderly}")


def display_survivors_per_age_group():
    children = 0
    adults = 0
    elderly = 0
    child_num_survived = 0
    ad_num_survived= 0
    eld_num_survived = 0
    for record in records:
        # solution copied from SOL
        if record[5] != "":
            age = float(record[5])
            if age < 18:
                children += 1
                survival_status = int(record[1])
                if survival_status == 1:
                    child_num_survived += 1
            elif age < 65:
                adults += 1
                survival_status = int(record[1])
                if survival_status == 1:
                    ad_num_survived += 1
            else:
                elderly += 1
                survival_status = int(record[1])
                if survival_status == 1:
                    eld_num_survived += 1
    print(f"Children: {child_num_survived}/{children}, Adults: {ad_num_survived}/{adults}, Elderly: {eld_num_survived}/{elderly}")


def display_menu():
    print("""
Please select of the following options:
[1] Display the names of all passengers
[2] Display the number of passengers that survived
[3] Display the number of passengers per gender
[4] Display the number of passengers per age group
[5] Display the number of survivors per age group""")
    choice = int(input())
    return choice


def run():
    load_data("titanic.csv")
    print(f"Successfully loaded {len(records)} records")
    selected_option = display_menu()
    print(f"You have selected option: {selected_option}")
    if selected_option == 1:
        display_passenger_names()
    elif selected_option == 2:
        display_num_survivors()
    elif selected_option == 3:
        display_passengers_per_gender()
    elif selected_option == 4:
        display_passengers_per_age_group()
    elif selected_option == 5:
        display_survivors_per_age_group()
    else:
        print("Error! Option not recognised!")


if __name__ == "__main__":
    run()
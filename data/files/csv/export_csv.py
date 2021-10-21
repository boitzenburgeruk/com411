import csv


def export(path, export_number):
    print("Exporting...")
    with open(path, "a") as file:
        reader = csv.reader(file)
        for x in range(0, export_number, 1):
            bot_id = int(input("Please assign an ID number: "))
            bot_name = str(input("Please enter the name for bot: "))
            bot_paint = str(input("Please enter what colour you would like the bot: "))
            file.write(f"\n{bot_id}, {bot_name}, {bot_paint}")
        file.close()
        print("Done!")


def run():
    export("exported_bots.csv", 2)


if __name__ == "__main__":
    run()
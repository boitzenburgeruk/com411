import json


def read(path):
    with open(path) as file:
        data = json.load(file)
        city = data["city"]
        population = data["population"]
        bots = data["bots"]
        print(f"City Name: {city}")
        print(f"Population Size: {population}")
        for bot in bots:
            name = bot["name"]
            stats = bot["stats"]
            print(f"{name} has the following stats: {stats}")
        file.close()


def run():
    read("robocity.json")


if __name__ == "__main__":
    run()

import json


def read(path):
    print("Reading...")
    with open(path, "r") as file:
        data = json.load(file)
    print("Done!")
    file.close()
    return data


def save(path, data):
    print("Exporting...")
    with open(path, "w") as file:
        json.dump(data, file, indent=4)
    print("Done!")
    file.close()


def run():
    json_data = read("robocity.json")
    save("exported.json", json_data)


if __name__ == "__main__":
    run()

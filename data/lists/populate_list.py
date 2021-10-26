def directions():
    directions = ["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions


def menu():
    print("Please select a direction:")
    list = directions()
    for index in range(len(list)):
        direction = list[index]
        print(f"{index}: {direction}")
    choice = int(input())
    choice = list[choice]
    return choice


def run():
    route = []
    print("Working out escape route...")
    for i in range(0, 5, 1):
        route.append(menu())
    print(f"Escape Route: {route[0]}, {route[1]}, {route[2]}, {route[3]}, {route[4]}")


if __name__ == "__main__":
    run()
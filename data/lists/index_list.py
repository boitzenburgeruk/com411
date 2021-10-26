def movements():
    path = ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path


def run():
    print("Moving...")
    list = movements()
    for i in range(0, len(list), 2):
        direction = list[i]
        steps = list[i+1]
        print(f"{direction} for {steps} steps")


if __name__ == "__main__":
    run()
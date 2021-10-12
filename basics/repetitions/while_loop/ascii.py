def run():
    count = 0
    bars = int(input("How many bars should be charged? "))

    while bars != count:
        count = count + 1
        print("Charging " + ("█" * count))

    print("\nThe battery is fully charged!")
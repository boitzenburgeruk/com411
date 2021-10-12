def run():
    def display_ladder(steps):
        for x in range(0, steps, 1):
            print("| |")
            print("***")
        print("| |")

    def create_ladder():
        steps = int(input("How many steps remain? "))
        display_ladder(steps)

    create_ladder()

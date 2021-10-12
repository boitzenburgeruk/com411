def run():
    initial_look = str(input("Where should I look? ").lower())

    if initial_look == "in the bedroom":
        bedroom_look = str(input("Where in the bedroom should I look? ").lower())
        if bedroom_look == "under the bed":
            print("Found some shoes! But no battery...")
        else:
            print("Found some mess, but no battery...")

    elif initial_look == "in the bathroom":
        bathroom_look = str(input("Where in the bathroom should I look? ").lower())
        if bathroom_look == "in the bathtub":
            print("Found a rubber duck! But no battery...")
        else:
            print("Found a wet surface, but no battery...")

    elif initial_look == "in the lab":
        lab_look = str(input("Where in the lab should I look? "))
        if lab_look == "on the table":
            print("Yes! I found my battery!")
        else:
            print("Found some tools, but no battery...")

    # will run if none of the values match the if statements
    else:
        print("I do not know where that is, but I will keep looking")
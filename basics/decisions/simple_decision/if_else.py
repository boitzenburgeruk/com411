def run():
    activity = str(input("Please enter an activity to be performed: ").lower())
    if activity == "calculate":
        print("Performing calculations...")
    else:
        print("Performing activity...")
    print("Activity completed!")
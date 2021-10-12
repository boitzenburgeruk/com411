def run():
    choice = str(input("What type of adventure should I have? "))

    if choice == "scary" or choice == "short":
        print("Entering the dark forest!")
    elif choice == "safe" or choice == "long":
        print("Taking the safe route!")
    else:
        print("Not sure which route to take...")
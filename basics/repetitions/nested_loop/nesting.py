# Solution copied from Solent Online Learning
def run():
    # Ask user for sequence and marker
    print("Please enter a sequence:")
    sequence = input()

    print("Please enter the character for the marker:")
    marker = input()

    # Find markers
    is_counting = False
    count = 0

    for character in sequence:
        if (is_counting == False) and (character == marker):
            print("Found first marker")
            is_counting = True
        elif (is_counting == True) and (character == marker):
            print("Found last marker")
        elif is_counting:
            count += 1

    # Display result
    print(f"The distance between the markers is {count}")

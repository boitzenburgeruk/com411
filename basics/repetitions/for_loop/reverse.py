def run():
    rev_string = ""
    string = str(input("What phrase do you see? "))
    print("\nReversing...")

    for count in range(len(string), 0, -1):
        rev_string = rev_string + str(string[count - 1])

    print(rev_string)
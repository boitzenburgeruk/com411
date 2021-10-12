def run():
    rev_string = ""
    string = str(input("What phrase do you see? "))
    print("\nReversing...")

    for character in string:
        rev_string = character + rev_string

    print(rev_string)
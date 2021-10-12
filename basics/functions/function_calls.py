def run():
    word = str(input("Please enter a word: "))
    print("\n1.) Display in a Box\n2.) Display Lower-case\n"
          "3.) Display Upper-case\n4.) Display Mirrored\n5.) Repeat\n")
    choice = int(input("How would you like to display this word? "))
    if choice == 1:
        in_box(word)
    elif choice == 2:
        lower_case(word)
    elif choice == 3:
        upper_case(word)
    elif choice == 4:
        mirror(word)
    elif choice == 5:
        repeat(word)


def repeat(word):
    # True = Upper, False = Lower
    case = True
    loop = int(input("How many times would you like the word displayed? "))
    for x in range(0, loop, 1):
        if case is True:
            print(word.upper())
            case = False
        elif case is False:
            print(word.lower())
            case = True


def mirror(word):
    rev_string = ""
    for count in range(len(word), 0, -1):
        rev_string = rev_string + str(word[count - 1])
    print(f"{word} | {rev_string}")


def lower_case(word):
    print(word.lower())


def upper_case(word):
    print(word.upper())


def in_box(word):
    message = f"* {word} *"
    print("*" * len(message))
    print(message)
    print("*" * len(message))


run()
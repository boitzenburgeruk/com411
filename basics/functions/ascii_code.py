def run():
    print("Program Started!")
    character = str(input("Please enter a standard character: "))
    if len(character) != 1:
        print("Error: character not inputted")
    else:
        ascii = ord(character)
        print(f"The ASCII code for {character} is {ascii}!")
    print("Program Ended!")
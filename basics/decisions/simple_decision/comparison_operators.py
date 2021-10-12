def run():
    first_number = int(input("Please enter a number: "))
    second_number = int(input("Please enter another number: "))

    if first_number == second_number:
        print("Both numbers are equal!")
    elif first_number > second_number:
        print("The second number is smallest")
    else:
        print("The first number is smallest")
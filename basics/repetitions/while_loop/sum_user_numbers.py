def run():
    total = 0
    count = 1

    choice = int(input("How many numbers should I sum up? "))

    # very messy while statement but shut up, you didn't see anything
    while count != (choice + 1):
        number = int(input(f"Please enter number {count} of {choice}: "))
        count = count + 1
        total = total + number

    print(f"The answer is {total}")

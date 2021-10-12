def run():
    odd_numbers = 0
    even_numbers = 0

    first_number = int(input("Please enter the first whole number: "))
    if first_number % 2 != 0:
        odd_numbers = odd_numbers + 1
    else:
        even_numbers = even_numbers + 1

    second_number = int(input("Please enter the second whole number: "))
    if second_number % 2 != 0:
        odd_numbers = odd_numbers + 1
    else:
        even_numbers = even_numbers + 1

    third_number = int(input("Please enter the third whole number: "))
    if third_number % 2 != 0:
        odd_numbers = odd_numbers + 1
    else:
        even_numbers = even_numbers + 1

    print(f"There were {even_numbers} even and {odd_numbers} odd numbers")
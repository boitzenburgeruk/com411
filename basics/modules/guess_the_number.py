def run():
    import random


    def play_guess_the_number(mini, max, number):
        still_guessing = True
        print(f"I am thinking of a number between {mini} and {max}!")
        while still_guessing is True:
            guess = int(input("Guess a number: "))
            if guess > number:
                print("Your guess is too high...")
            elif guess < number:
                print("Your guess is too low...")
            else:
                still_guessing = False
                print("Congratulations! You guessed my number!")

    minimum = int(input("Please enter the minimum value: "))
    maximum = int(input("Please enter the maximum value: "))

    random_number = random.randrange(minimum, maximum)
    play_guess_the_number(minimum, maximum, random_number)
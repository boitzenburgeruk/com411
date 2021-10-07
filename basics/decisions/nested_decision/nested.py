cover = str(input("What type of cover does the book have? ").lower())

if cover == "soft":
    answer = str(input("Is the book perfect-bound? ").lower())
    if answer == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
elif cover == "hard":
    print("Books with hard covers can be more expensive!")

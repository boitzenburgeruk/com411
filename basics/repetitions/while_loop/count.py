counter = 0
avoid = int(input("How many live cables should I avoid? "))

while avoid != counter:
    counter = counter + 1
    print(f"Avoiding... Done! {counter} live cables avoided!")

print("\nAll live cables have been avoided!")

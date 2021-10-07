brightness = int(input("What level of brightness is required? "))
print("Adjusting brightness...\n")

# the argument 'brightness + 1' was the only way I could get this to work properly
for count in range(2, brightness + 1, 2):
    print("Beep's Brightness Level: " + ("*" * count))
    print("Bop's Brightness Level: " + ("*" * count) + "\n")

print("\nAdjustments complete!")
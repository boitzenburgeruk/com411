print("Program Started!")
ascii_code = abs(int(input("Please enter an ASCII code: ")))

if ascii_code in range(32, 127):
    character = chr(ascii_code)
    print(f"The character represented by the ASCII code {ascii_code} is: {character}")
    if ascii_code == 32:
        print("32 in ASCII represents a space!")
else:
    print("Error: ASCII code not in range")
print("Program Ended!")

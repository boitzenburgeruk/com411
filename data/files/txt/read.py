def display_chars(path, number_of_chars):
    file = open(path)
    output = file.read(number_of_chars)
    print(f"The first five characters are:\n{output}")
    file.close()


def display_line(path):
    file = open(path)
    output = file.readline()
    print(f"\nThe first line is:\n{output}")
    file.close()


def display_text(path):
    file = open(path)
    output = file.read()
    print(f"The full text is:\n{output}")
    file.close()


def run():
    path = "library.txt"
    display_chars(path, 5)
    display_line(path)
    display_text(path)


if __name__ == "__main__":
    run()

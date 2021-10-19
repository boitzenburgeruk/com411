def search(path):
    print("Searching...")
    file = open(path)
    for line in file:
        print(f"Looked in {line}")
    print("...Done!")
    file.close()


def run():
    search("library.txt")


if __name__ == "__main__":
    run()
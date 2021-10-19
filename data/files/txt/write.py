def search(path):
    print("Searching...")
    sections = ""
    books = "Books:\n"
    file = open(path)
    for line in file:
        if line[0:7] == "Section":
            sections = sections + line
        else:
            books = books + line
    file.close()
    print("...Done!")
    single_string = (sections + "\n" + books)
    return single_string


def save(path, data):
    print("Saving...")
    file = open(path, "w")
    file.write(data)
    file.close()
    print("...Done!")


def run():
    data = search("books.txt")
    save("section-books.txt", data)


if __name__ == "__main__":
    run()
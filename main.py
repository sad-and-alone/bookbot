def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #print(text)
    words = text.split()
    print(len(words))


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
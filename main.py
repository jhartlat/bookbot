def count_characters(text):

    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char.lower()] = 1
            continue

        char_count[char.lower()] += 1

    return char_count

def main():

    with open('books/frankenstein.txt') as book:
        book_contents = book.read()


    char_count = count_characters(book_contents)
    for char in char_count:
        print(f'{char}: {char_count[char]}')


main()

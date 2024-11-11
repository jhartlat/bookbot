def count_characters(text):

    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char.lower()] = 1
            continue

        char_count[char.lower()] += 1

    return char_count


def print_report(filepath, char_count):

    print(f'--- Begin report of {filepath} ---')

    words = char_count[' ']
    print(f'{words:,} words found in the document' + '\n')

    a_z = 'abcdefghijklmnopqrstuvwxyz'
    for char in a_z:
        if char in char_count:
            print(f'The letter \'{char}\' was found {char_count[char]:,} times')

    print('--- End Report ---')


def main():

    filepath = 'books/frankenstein.txt'
    with open(filepath) as file:
        text = file.read()

    char_count = count_characters(text)
    print_report(filepath, char_count)


main()

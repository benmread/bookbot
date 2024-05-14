import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    print(len(wordcount(file_contents)))
    charactercount(file_contents)

def wordcount(text):
    return text.split()

def charactercount(text):
    char_counter = {}
    text = text.lower()

    for letter in string.printable: # all ASCII characters
        if letter in text and letter not in char_counter:
            char_counter[letter] = text.count(letter)

    char_list = char_counter.items()
    char_list.sort(reverse=True)
    print(char_list)


main()
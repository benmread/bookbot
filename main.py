import string

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    sorted = sortedlist(charactercount(file_contents))

    # report
    print("--- Begin report of books/frankenstein.txt ---")
    print(str(len(wordcount(file_contents))) + " words found in document\n")
    for item in sorted:
        if item["char"].isalpha(): # skip all the symbols
            print(f"The '{item["char"]}' character was found {str(item["num"])} times")
    print("--- End report ---")


def wordcount(text):
    return text.split()


def charactercount(text):
    char_counter = {}
    char_list = []
    text = text.lower()

    for letter in string.printable: # all ASCII characters
        if letter in text and letter not in char_counter:
            char_counter[letter] = text.count(letter)

    return char_counter


def sortedlist(char_dict):
    sorted_list = []
    for key in char_dict:
        sorted_list.append({"char": key, "num": char_dict[key]})

    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]


main()
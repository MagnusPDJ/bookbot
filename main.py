def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_characters = get_character_num(text)
    list_of_dict = convert_dict_to_list(num_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    print()
    character_data(list_of_dict)
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book):
    words = book.split()
    return len(words)

def get_character_num(book):
    num_characters = {}
    for c in book:
        lowered = c.lower()
        if lowered in num_characters:
            num_characters[lowered] += 1
        else:
            num_characters[lowered] = 1
    return num_characters

def convert_dict_to_list(dict):
    list_of_dict = []
    for char in dict:
        list_of_dict.append({"char": char, "count": dict[char]})

    def sort_on(list_of_dict):
        return  list_of_dict["count"]
    list_of_dict.sort(reverse=True, key=sort_on)

    return list_of_dict

def character_data(list_of_dict):
    for dict in list_of_dict:
        if not dict["char"].isalpha():
            continue
        print(f"The '{dict['char']}' character was found {dict['count']} times")
main()
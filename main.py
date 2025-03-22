from stats import word_count
from stats import get_character_num
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = word_count(text)
    num_characters = get_character_num(text)
    list_of_dict = convert_dict_to_list(num_characters)

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print(f"----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print(f"--------- Character Count -------")
    character_data(list_of_dict)
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

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
        print(f"{dict['char']}: {dict['count']}")

main()
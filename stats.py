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
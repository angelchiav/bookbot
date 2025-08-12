def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def get_num_words(text):
    words = len(text.split())
    print(f"Found {words} total words")
    return words

def get_num_letters(text):
    result = {}
    for letter in text:
        if letter.lower() not in result:
            result[letter.lower()] = 0
        result[letter.lower()] += 1
    return result

def sort_on(letter_dict):
    return letter_dict["num"]

def dict_list(letter_dict):
    letter_list = []
    for key, value in letter_dict.items():
        if key.isalpha():
            letter_list.append({"char": key, "num": value})
    return letter_list
import sys

from stats import (
    get_num_words, 
    get_num_letters,
    get_book_text,
    dict_list,
    sort_on
)

def main():
    try:
        book_text = get_book_text(sys.argv[1])
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")
    print(f"----------- Word Count ----------")
    get_num_words(book_text)
    print(f"--------- Character Count -------")
    book_letters = get_num_letters(book_text)
    lst = dict_list(book_letters)
    lst.sort(reverse=True, key=sort_on)
    for item in lst:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")
    
main()
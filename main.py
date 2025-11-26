import sys
from stats import get_num_words, get_characters_frequency, get_sorted_list_of_characters

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents=f.read()
        return file_contents

def main():
    if len(sys.argv)==2:
        book_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_characters_frequency(text)
    sorted_list=get_sorted_list_of_characters(characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")

main()
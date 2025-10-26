import sys
from stats import word_count, char_count, sort_dict

def get_book_txt(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(path, count, char_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in char_counts:
        letter = item["char"]
        qty = item["num"]
        if letter.isalpha():
            print(f"{letter}: {qty}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]

    book = get_book_txt(path)
    count = word_count(book)
    char_counts = char_count(book)
    char_counts = sort_dict(char_counts)
    print_report(path, count, char_counts)

main()
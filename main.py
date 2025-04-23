import sys
from stats import word_count, char_count, char_count_sorted





def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]

    def get_book_text():

        with open(book_path, "r") as f:
            file_content = f.read()
            return file_content
        
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count(get_book_text())} total words")
    print("----------- Character Count -----------")
    #print(f"{char_count(get_book_text())}")
    for char in char_count_sorted(get_book_text()):
        print(f"{char['name']}: {char['num']}")
    print("============= END ===============")



if __name__ == "__main__":
    main()
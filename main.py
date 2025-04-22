from stats import word_count, char_count, char_count_sorted

book_path = "./books/frankenstein.txt"


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